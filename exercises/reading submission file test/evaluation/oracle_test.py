# We importeren wat hulpklassen uit TESTed.
from evaluation_utils import EvaluationResult, Message
import os

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

# De orakelfunctie heeft altijd minstens één argument:
# - de "context", een object met wat metadata (zie hieronder)
# - de overige argumenten zijn die uit het testplan
#   (de getallen 5 en 6 in dit geval)
def evaluate_test(context, som):
    submission = get_submission_code()
    correct = (("10" not in submission) and ("+" in submission) and (som == 10))
    mymessages = []
    if correct:
        expected = 10
        mymessages.append(Message("Goed zo! Je hebt de computer 10 laten berekenen."))
    else:
        expected = 10
        mymessages.append(Message("Je moet een optelling gebruiken om 10 te krijgen."))

    return EvaluationResult(
      # Boolean of dat het resultaat juist is
      result = correct,
      # De "verwachte waarde" om te tonen op Dodona
      dsl_expected = repr(expected),
      # De eigenlijke waarde uit de oplossing om te tonen op Dodona
      dsl_actual = repr(context.actual),
      # Optionale lijst van berichten om te tonen op Dodona
      messages = mymessages
    )