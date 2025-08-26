from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def evaluate_test(context, var):
    submission = get_submission_code()
    submission_as_lines = submission.splitlines()
    counters = [0, 0] # [pluses, minuses]
    answer_not_used = True

    for line in submission_as_lines:
        if var in line and str(context.expected) in line:
            answer_not_used = False
        if var is "symbolcheck" and "+" in line:
            counters[0] += 1
        if var is "symbolcheck" and "-" in line:
            counters[1] += 1 

    mymessages = []
    if var is "symbolcheck":
        correct = counters[0] >= 1 and counters[1] >= 1
        actual = f"{counters[0]}/{counters[1]}"
        if counters[0] < 1:
            mymessages.append(Message(f"Je moet minstens één optelling gebruiken."))
        if counters[1] < 1:
            mymessages.append(Message(f"Je moet minstens één aftrekking gebruiken."))
    else:
        checks = [answer_not_used,
                  context.actual == context.expected,
                  type(context.actual) == type(context.expected)]
        correct = all(checks)
        actual = context.actual
        if correct:
            mymessages.append(Message(f"Goed zo! Je hebt de computer {context.expected} laten berekenen."))
        else:
            if not checks[0]:
                mymessages.append(Message(f"Je mag het getal {context.expected} niet gebruiken voor de variabele {var}."))
            if not checks[1]:
                mymessages.append(Message(f"De waarde voor {var} is niet wat we verwachtten."))
            if not checks[2]:
                types = {int: "integer (geheel getal)", float: "float (kommagetal)", str: "string (tekst)"}
                mymessages.append(Message(f"{context.expected} is een {types[type(context.expected)]}. Je moet dus dezelfde datatype gebruiken om dat te krijgen."))

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(actual),
      messages = mymessages
    )