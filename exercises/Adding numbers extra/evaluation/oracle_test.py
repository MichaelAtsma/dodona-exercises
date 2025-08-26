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
def evaluate_test(context, var):
    submission = get_submission_code()
    submission_as_lines = submission.splitlines()
    correct = True
    counters = [0, 0] # [pluses, minuses]

    for line in submission_as_lines:
        if var in line and str(context.expected) in line:
            correct = False
        if var is "d" and "+" in line:
            counters[0] += 1
        if var is "d" and "-" in line:
            counters[1] += 1 

    mymessages = []
    if var is "d":
        correct = counters[0] >= 1 and counters[1] >= 1
        actual = f"{counters[0]} optelling(en) en {counters[1]} aftrekking(en) gebruikt."
        if counters[0] < 1:
            mymessages.append(Message(f"Je moet minstens één optelling gebruiken."))
        if counters[1] < 1:
            mymessages.append(Message(f"Je moet minstens één aftrekking gebruiken."))
    else:
        correct = correct and (context.actual == context.expected)
        actual = context.actual
        if correct:
            mymessages.append(Message(f"Goed zo! Je hebt de computer {context.expected} laten berekenen."))
        else:
            mymessages.append(Message(f"Je moet {context.expected} opslaan in de variabele {var} zonder het getal {context.expected} te gebruiken."))

    return EvaluationResult(
      # Boolean of dat het resultaat juist is
      result = correct,
      # De "verwachte waarde" om te tonen op Dodona
      dsl_expected = repr(context.expected),
      # De eigenlijke waarde uit de oplossing om te tonen op Dodona
      dsl_actual = repr(actual),
      # Optionale lijst van berichten om te tonen op Dodona
      messages = mymessages
    )