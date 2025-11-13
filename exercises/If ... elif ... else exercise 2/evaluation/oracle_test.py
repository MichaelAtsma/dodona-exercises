from evaluation_utils import EvaluationResult, Message # type: ignore
import re

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, match_regex, condition1, condition2, correct_message_template, wrong_values_with_message_template):
    submission = get_submission_code()
    checks = {}
    checks["correct value"] = context.actual == context.expected

    m = re.fullmatch(match_regex, submission)
    value_of_score = m.group(1) if m else ""
    checks["code matches regex"] = m is not None

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(correct_message_template.format(condition1, condition2, value_of_score)))
    else:
        if not checks["correct value"]:
            mymessages.append(Message(wrong_values_with_message_template[context.actual].format(condition1, condition2, value_of_score)))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel de voorwaarde aanpassen. Zorg ervoor dat je de rest van de code niet wijzigt."))
        
    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )