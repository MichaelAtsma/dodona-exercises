from evaluation_utils import EvaluationResult, Message # type: ignore
import re

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, forbidden_texts_and_descriptions):
    submission = get_submission_code()
    checks = {}
    checks["correct value"] = context.actual == context.expected

    used_forbidden_texts_and_descriptions = {}
    checks["forbidden text not used"] = True
    for forbidden_text in forbidden_texts_and_descriptions.keys():
        if forbidden_text in submission:
            checks["forbidden text not used"] = False
            used_forbidden_texts_and_descriptions[forbidden_text] = forbidden_texts_and_descriptions[forbidden_text]
    
    correct = all(checks.values())
    mymessages = []
    if not checks["forbidden text not used"]:
        mymessages.append(Message(f"Je mag geen gebruik maken van: {', '.join(used_forbidden_texts_and_descriptions.values())}."))

    return EvaluationResult(
      result = correct,
      dsl_expected = "", # empty string reverts to default rendering of expected value
      dsl_actual = "", # empty string reverts to default rendering of actual value
      messages = mymessages
    )