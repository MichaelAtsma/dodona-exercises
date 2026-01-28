from evaluation_utils import EvaluationResult, Message # type: ignore
import re

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, match_regex):
    submission = get_submission_code()
    checks = {}
    checks["correct value"] = context.actual == context.expected

    m = re.fullmatch(match_regex, submission)
    student_contribution = m.group(1) if m else ""
    checks["code matches regex"] = m is not None

    checks["does not have too many print statements"] = submission.count("print(") <= 50

    correct = all(checks.values())
    mymessages = []
    if not checks["correct value"]:
        mymessages.append(Message("De output van je programma is niet correct."))
    if not checks["code matches regex"]:
        mymessages.append(Message("Je gebruikt niet de juiste structuur in je code. Zorg ervoor dat je een for-lus gebruikt."))
    if not checks["does not have too many print statements"]:
        mymessages.append(Message("Je gebruikt te veel print-statements. Zorg dat je de for-lus gebruikt in plaats van letterlijk elke regel te printen."))

    return EvaluationResult(
      result = correct,
      dsl_expected = "", # empty string seems to default to correct display
      dsl_actual = "", # empty string seems to default to correct display
      messages = mymessages
    )