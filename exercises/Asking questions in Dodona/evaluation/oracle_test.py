# We importeren wat hulpklassen uit TESTed.
from evaluation_utils import EvaluationResult, Message

# De orakelfunctie heeft altijd minstens één argument:
# - de "context", een object met wat metadata (zie hieronder)
# - de overige argumenten zijn die uit het testplan
#   (de getallen 5 en 6 in dit geval)
def evaluate_test(context, secret_number):
    correct = secret_number == context.actual
    if correct:
        display_text = "Goed zo! Je hebt het geheime getal gevonden."
    else:
        display_text = "De waarde van het geheime getal kan je enkel krijgen door een vraag te stellen via Dodona."
    return EvaluationResult(
      # Boolean of dat het resultaat juist is
      result = correct,
      # De "verwachte waarde" om te tonen op Dodona
      dsl_expected = repr(display_text),
      # De eigenlijke waarde uit de oplossing om te tonen op Dodona
      dsl_actual = repr(context.actual),
      # Optionale lijst van berichten om te tonen op Dodona
      messages = [Message("Test")]
    )