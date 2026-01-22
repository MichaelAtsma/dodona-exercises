from evaluation_utils import EvaluationResult, Message # type: ignore
import re
import os

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def get_boilerplate():
    pass # it is impossible to access the boilerplate file from here
    # with open("../judge/.editorconfig", 'r') as f:
    #     return f.read()
    # return os.path.abspath("../") # cannot access higher than /mnt/

# The directory structure is as follows:
# /       (cannot access higher than this folder)
# - bin/ and a bunch of other system folders
# - mnt/
#   - workdir/
#     - common/
#       - values.pyc
#       - execution_0.py
#       - submission.py
#       - submission.pyc
#       - evaluation_utils.py
#       - values.py
#       - evaluation_utils.pyc
#       - execution_0.pyc
#     - execution_0/
#   - submissionID(probably)/
#     - submission/
#       - source    (the student's submitted code)
#     - resources/
#       - suite.yaml
#       - oracle_test.py
#     - judge/
#       - tested/   (a lot of stuff I don't need)
#       - .editorconfig  (not useful file)


def get_ast_translator_code():
    with open("../judge/tested/dsl/ast_translator.py", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test(context, match_regex, mandatory_logical_operators_and_descriptions, correct_message_template, wrong_value_message_template):
    # submission = get_submission_code()
    # checks = {}
    # checks["correct value"] = context.actual == context.expected

    # m = re.fullmatch(match_regex, submission)
    # student_contribution = m.group(1) if m else ""
    # checks["code matches regex"] = m is not None

    # checks["student contribution type is not string"] = '"' not in student_contribution and "'" not in student_contribution

    # checks["mandatory logical operators used"] = True
    # for operator in mandatory_logical_operators_and_descriptions.keys():
    #     if operator not in student_contribution:
    #         checks["mandatory logical operators used"] = False

    # correct = all(checks.values())
    # mymessages = [get_boilerplate()]
    # if correct:
    #     mymessages.append(Message(correct_message_template.format(student_contribution)))
    # else:
    #     if not checks["correct value"]:
    #         mymessages.append(Message(wrong_value_message_template.format(student_contribution)))
    #     if not checks["mandatory logical operators used"]:
    #         missing_operators = [desc for op, desc in mandatory_logical_operators_and_descriptions.items() if op not in student_contribution]
    #         mymessages.append(Message(f"Je moet in je voorwaarde gebruikmaken van: {', '.join(missing_operators)}."))
    #     if not checks["code matches regex"]:
    #         mymessages.append(Message(f"Je mag enkel de voorwaarde aanpassen. Zorg ervoor dat je de rest van de code niet wijzigt."))
    #     if not checks["student contribution type is not string"]:
    #         mymessages.append(Message(f"Hoewel de uitkomst misschien correct is, moet je een getal printen, dan heb je dus geen aanhalingstekens nodig."))
    
    mymessages = []
    correct = False
    mymessages.append(Message("Hieronder de file ast_translator.py voor je referentie:"))
    for line in get_ast_translator_code().splitlines():
        mymessages.append(Message(line))
    
    expected = "testingline1\\ntestingline2\\ntestingline3".encode().decode('unicode_escape')
    actual = "testingline1testingline2"

    return EvaluationResult(
      result = correct,
      dsl_expected = expected,
      dsl_actual = actual,
      messages = mymessages
    )