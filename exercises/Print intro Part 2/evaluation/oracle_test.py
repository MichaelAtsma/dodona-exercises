from evaluation_utils import EvaluationResult, Message # type: ignore
import re

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, match_regex, mandatory_logical_operators_and_descriptions, correct_message_template, wrong_value_message_template):
    submission = get_submission_code()
    checks = {}
    checks["correct value"] = context.actual == context.expected

    m = re.fullmatch(match_regex, submission)
    student_contribution = m.group(1) if m else ""
    checks["code matches regex"] = m is not None

    checks["mandatory logical operators used"] = True
    for operator in mandatory_logical_operators_and_descriptions.keys():
        if operator not in student_contribution:
            checks["mandatory logical operators used"] = False

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(correct_message_template.format(student_contribution)))
    else:
        if not checks["correct value"]:
            mymessages.append(Message(wrong_value_message_template.format(student_contribution)))
        if not checks["mandatory logical operators used"]:
            missing_operators = [desc for op, desc in mandatory_logical_operators_and_descriptions.items() if op not in student_contribution]
            mymessages.append(Message(f"Je moet in je voorwaarde gebruikmaken van: {', '.join(missing_operators)}."))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel iets tussen de haakjes schrijven. Zorg ervoor dat je de rest van de code niet wijzigt."))
        
    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )