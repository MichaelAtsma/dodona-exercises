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
    student_for_variable = m.group(1) if m else ""
    student_start = m.group(2) if m else ""
    student_end = m.group(3) if m else ""
    student_printed_variable = m.group(4) if m else ""
    checks["code matches regex"] = m is not None
    
    student_contribution = "\n".join([student_for_variable, student_start, student_end, student_printed_variable])

    checks["for variable matches printed variable"] = student_for_variable == student_printed_variable if checks["code matches regex"] else True

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

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(correct_message_template))
    else:
        if not checks["correct value"]:
            mymessages.append(Message(wrong_value_message_template))
        if not checks["mandatory texts used"]:
            mymessages.append(Message(f"Je moet gebruik maken van: {', '.join(missing_texts_and_descriptions.values())}."))
        if not checks["forbidden text not used"]:
            mymessages.append(Message(f"Je mag geen gebruik maken van: {', '.join(used_forbidden_texts_and_descriptions.values())}."))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel de underscores vervangen. Zorg ervoor dat je de rest van de code niet wijzigt."))
        if not checks["for variable matches printed variable"]:
            mymessages.append(Message(f"Je moet ervoor zorgen dat de variabele achter het woord 'for' van de for-lus overeenkomt met de variabele die je print binnen in de lus."))

    return EvaluationResult(
      result = correct,
      dsl_expected = "", # empty string seems to default to correct display
      dsl_actual = "", # empty string seems to default to correct display
      messages = mymessages
    )