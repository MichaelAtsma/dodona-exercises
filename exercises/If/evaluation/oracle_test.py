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

    match = re.fullmatch(match_regex, submission)
    checks["code matches regex"] = match is not None

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(f"Goed zo! Je hebt een ware uitspraak gemaakt waardoor de regel onder de if-statement werd uitgevoerd."))
    else:
        if not checks["correct value"]:
            mymessages.append(Message(f"Helaas werd de regel onder de if-statement niet uitgevoerd. Kijk nog eens goed naar je voorwaarde."))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel de voorwaarde aanpassen. Zorg ervoor dat je de rest van de code niet wijzigt."))
        
    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )