# We importeren wat hulpklassen uit TESTed.
from evaluation_utils import EvaluationResult, Message

# De orakelfunctie heeft altijd minstens één argument:
# - de "context", een object met wat metadata (zie hieronder)
# - de overige argumenten zijn die uit het testplan
#   (de getallen 5 en 6 in dit geval)
def evaluate_test(context, submissionfile, som):
    submission = submissionfile.read()
    correct = (("10" not in submission) and (som == 10))
    if correct:
        display_text = 10
        message = Message("Goed zo! Je hebt het geheime getal gevonden.")
    else:
        display_text = "?"
        message = Message("De waarde van het geheime getal kan je enkel krijgen door een vraag te stellen via Dodona.")

    return EvaluationResult(
      # Boolean of dat het resultaat juist is
      result = correct,
      # De "verwachte waarde" om te tonen op Dodona
      dsl_expected = repr(display_text),
      # De eigenlijke waarde uit de oplossing om te tonen op Dodona
      dsl_actual = repr(context.actual),
      # Optionale lijst van berichten om te tonen op Dodona
      messages = [message]
    )