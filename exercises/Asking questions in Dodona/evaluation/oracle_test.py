# We importeren wat hulpklassen uit TESTed.
from evaluation_utils import EvaluationResult, Message
from datetime import datetime

# De orakelfunctie heeft altijd minstens één argument:
# - de "context", een object met wat metadata (zie hieronder)
# - de overige argumenten zijn die uit het testplan
#   (de getallen 5 en 6 in dit geval)
def evaluate_test(context, secret_number):
    return EvaluationResult(
      # Boolean of dat het resultaat juist is
      result = secret_number == context.actual,
      # De "verwachte waarde" om te tonen op Dodona
      dsl_expected = "De waarde van het geheime getal kan je enkel krijgen door een vraag te stellen via Dodona.",
      # De eigenlijke waarde uit de oplossing om te tonen op Dodona
      dsl_actual = repr(context.actual),
      # Optionale lijst van berichten om te tonen op Dodona
      messages = []
    )