from evaluation_utils import EvaluationResult, Message # type: ignore
import re

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, match_regex, mandatory_texts_and_descriptions, forbidden_texts_and_descriptions, correct_message_template, wrong_value_message_template):
    submission = get_submission_code()
    checks = {}
    checks["correct value"] = context.actual == context.expected

    m = re.fullmatch(match_regex, submission)
    student_contribution = m.group(1) if m else ""
    checks["code matches regex"] = m is not None

    checks["student contribution type is not string"] = '"' not in student_contribution and "'" not in student_contribution

    missing_texts_and_descriptions = {}
    checks["mandatory texts used"] = True
    for text in mandatory_texts_and_descriptions.keys():
        if text not in student_contribution:
            checks["mandatory texts used"] = False
            missing_texts_and_descriptions[text] = mandatory_texts_and_descriptions[text]

    used_forbidden_texts_and_descriptions = {}
    checks["forbidden text not used"] = True
    for forbidden_text in forbidden_texts_and_descriptions.keys():
        if forbidden_text in student_contribution:
            checks["forbidden text not used"] = False
            used_forbidden_texts_and_descriptions[forbidden_text] = forbidden_texts_and_descriptions[forbidden_text]
    
    # count repetitions in expected and actual
    expected_repetitions = len(context.expected.splitlines())
    actual_repetitions = len(context.actual.splitlines())

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(correct_message_template.format(actual_repetitions)))
    else:
        if not checks["correct value"]:
            mymessages.append(Message(wrong_value_message_template.format(actual_repetitions, expected_repetitions)))
        if not checks["mandatory texts used"]:
            mymessages.append(Message(f"Je moet gebruik maken van: {', '.join(missing_texts_and_descriptions.values())}."))
        if not checks["forbidden text not used"]:
            mymessages.append(Message(f"Je mag geen gebruik maken van: {', '.join(used_forbidden_texts_and_descriptions.values())}."))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel iets tussen de haakjes schrijven. Zorg ervoor dat je de rest van de code niet wijzigt."))
        if not checks["student contribution type is not string"]:
            mymessages.append(Message(f"Je hebt een getal nodig in de range-functie, geen tekst."))
        
    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )