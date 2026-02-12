from evaluation_utils import EvaluationResult, Message # type: ignore
import re

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, match_regex, mandatory_texts_and_descriptions, forbidden_texts_and_descriptions, match_group_index_and_message_templates, correct_message_template, wrong_value_message_template):
    submission = get_submission_code()
    checks = {}
    try:
        checks["correct value"] = abs(float(context.actual) - float(context.expected)) < 1e-5
    except:
        checks["correct value"] = context.actual == context.expected

    m = re.fullmatch(match_regex, submission)
    student_contributions = [m.group(i) if m else "" for i in range(1, len(m.groups()) + 1)] if m else []
    checks["code matches regex"] = m is not None

    missing_texts_and_descriptions = {}
    checks["mandatory texts used"] = True
    for text in mandatory_texts_and_descriptions.keys():
        if not any(text in contribution for contribution in student_contributions):
            checks["mandatory texts used"] = False
            missing_texts_and_descriptions[text] = mandatory_texts_and_descriptions[text]

    used_forbidden_texts_and_descriptions = {}
    checks["forbidden text not used"] = True
    for forbidden_text in forbidden_texts_and_descriptions.keys():
        if any(forbidden_text in contribution for contribution in student_contributions):
            checks["forbidden text not used"] = False
            used_forbidden_texts_and_descriptions[forbidden_text] = forbidden_texts_and_descriptions[forbidden_text]

    correct = all(checks.values())
    mymessages = []
    if correct:
        actual_value_displayed = context.expected
        mymessages.append(Message(correct_message_template))
    else:
        actual_value_displayed = context.actual
        if not checks["correct value"]:
            mymessages.append(Message(wrong_value_message_template))
        if not checks["mandatory texts used"]:
            mymessages.append(Message(f"Je moet gebruik maken van: {', '.join(set(missing_texts_and_descriptions.values()))}."))
        if not checks["forbidden text not used"]:
            mymessages.append(Message(f"Je mag geen gebruik maken van: {', '.join(set(used_forbidden_texts_and_descriptions.values()))}."))
        if not checks["code matches regex"]:
            mymessages.append(Message(f"Je mag enkel de underscores vervangen. Zorg ervoor dat je de rest van de code niet wijzigt."))
    if checks["code matches regex"]:
        for index, message_template in match_group_index_and_message_templates.items():
            if index <= len(student_contributions):
                mymessages.append(Message(message_template.format(student_contributions[index - 1].strip())))


    return EvaluationResult(
      result = correct,
      readable_expected = context.expected,
      readable_actual = actual_value_displayed,
      messages = mymessages
    )