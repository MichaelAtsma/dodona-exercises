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
    condition = m.group(1) if m else ""
    checks["code matches regex"] = m is not None

    checks["mandatory logical operators used"] = True
    operators_not_used = []
    for operator in mandatory_logical_operators_and_descriptions.keys():
        if operator not in condition:
            checks["mandatory logical operators used"] = False
            operators_not_used.append(operator)

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(correct_message_template.format(condition)))
    else:
        if not checks["correct value"]:
            mymessages.append(Message(wrong_value_message_template.format(condition)))
        if not checks["mandatory logical operators used"]:
            mymessages.append(Message(f"Debugging: je voorwaarde is: {condition}"))
            missing_operators = [mandatory_logical_operators_and_descriptions[op] for op in operators_not_used]
            mymessages.append(Message(f"Je moet in je voorwaarde gebruikmaken van: {', '.join(missing_operators)}."))
            if missing_operators == ["<"] and ">" in condition:
                mymessages.append(Message(f"Sorry, je programma en je voorwaarde kloppen waarschijnlijk, maar je moet het symbool '<' gebruiken in plaats van '>', omdat ik geen tijd en/of zin heb om uit te zoeken hoe ik alle mogelijke vergelijkingsoperatoren kan toestaan."))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel de voorwaarde aanpassen. Zorg ervoor dat je de rest van de code niet wijzigt."))
        
    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )