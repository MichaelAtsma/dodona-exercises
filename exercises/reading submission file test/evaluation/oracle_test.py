# We importeren wat hulpklassen uit TESTed.
from evaluation_utils import EvaluationResult, Message
import os
import dis
import sys

# De orakelfunctie heeft altijd minstens één argument:
# - de "context", een object met wat metadata (zie hieronder)
# - de overige argumenten zijn die uit het testplan
#   (de getallen 5 en 6 in dit geval)
def evaluate_test(context):
    correct = False
    submission_file_directory = context.execution_directory
    files = os.listdir("../resources")
    files_as_text = "\n".join(files)
    # submission_file_path = os.path.join(submission_file_directory, "submission.py")
    # submission_file = open(submission_file_path, "r")
    # submission_content = submission_file.read()
    # submission_text = submission_content.decode("latin-1", errors="replace")
    # correct = (("10" not in submission_content) and (som == 10))
    mymessages = []
    if correct:
        display_text = 10
        mymessages.append(Message("Goed zo! Je hebt het geheime getal gevonden."))
    else:
        display_text = "?" # submission_content
        # mymessages.append(Message("hoi"))
        # mymessages.append(Message(type(context.actual)))
        for filename in files:
            mymessages.append(Message(filename))
        mymessages.append(Message(submission_file_directory))

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