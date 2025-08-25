# We importeren wat hulpklassen uit TESTed.
from evaluation_utils import EvaluationResult, Message
import os
import pandas

# De orakelfunctie heeft altijd minstens één argument:
# - de "context", een object met wat metadata (zie hieronder)
# - de overige argumenten zijn die uit het testplan
#   (de getallen 5 en 6 in dit geval)
def evaluate_test(context):
    correct = False
    submission_file_directory = context.execution_directory
    submission_file_path = os.path.join(submission_file_directory, "submission.pyc")
    submission_file = open(submission_file_path, "rb")
    # submission_content = submission_file.read()
    # correct = (("10" not in submission_content) and (som == 10))
    mymessages = []
    if correct:
        display_text = 10
        mymessages.append(Message("Goed zo! Je hebt het geheime getal gevonden."))
    else:
        display_text = "?" # submission_content
        # mymessages.append(Message("hoi"))
        # mymessages.append(Message(type(context.actual)))
        # mymessages.append(Message(submission_file))

    return EvaluationResult(
      # Boolean of dat het resultaat juist is
      result = correct,
      # De "verwachte waarde" om te tonen op Dodona
      dsl_expected = repr(display_text),
      # De eigenlijke waarde uit de oplossing om te tonen op Dodona
      dsl_actual = repr(context.actual),
      # Optionale lijst van berichten om te tonen op Dodona
      messages = mymessages
    )