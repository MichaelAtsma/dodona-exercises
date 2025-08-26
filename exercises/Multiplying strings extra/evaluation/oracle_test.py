from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def repetition_counter(string):
    for repeated_part_length in range(1, len(string)):
        if string == string[:repeated_part_length] * (len(string) // repeated_part_length):
            return string[:repeated_part_length], len(string)//repeated_part_length
    return string, len(string)

def evaluate_test(context, var):
    submission = get_submission_code()
    submission_as_lines = submission.splitlines()
    counters = [0, 0, 0, 0] # [multiplications, divisions, additions, subtractions]
    answer_not_used = True
    repeated_word, repetitions = repetition_counter(context.expected)
    correct_multiplication_used = False

    for line in submission_as_lines:
        if var in line and str(context.expected) in line:
            answer_not_used = False
        if var in line and str(repetitions) in line:
            correct_multiplication_used = True
        if var is "symbolcheck" and "*" in line:
            counters[0] += line.count("*")
        if var is "symbolcheck" and "/" in line:
            counters[1] += line.count("/")
        if var is "symbolcheck" and "+" in line:
            counters[2] += line.count("+")
        if var is "symbolcheck" and "-" in line:
            counters[3] += line.count("-")

    mymessages = []
    if var is "symbolcheck":
        correct = counters[0] >= 1 and counters[1] == 0 and counters[2] == 0 and counters[3] == 0
        actual = f"{counters[0]}*"
        if counters[0] < 1:
            mymessages.append(Message(f"Je moet minstens één vermenigvuldiging gebruiken."))
        if counters[1] > 0:
            actual += f",{counters[2]}/"
            mymessages.append(Message(f"Je mag geen delingen gebruiken."))
        if counters[2] > 0:
            actual += f",{counters[2]}+"
            mymessages.append(Message(f"Je mag geen optellingen gebruiken."))
        if counters[3] > 0:
            actual += f",{counters[3]}-"
            mymessages.append(Message(f"Je mag geen aftrekkingen gebruiken."))
    else:
        checks = [answer_not_used,
                  context.actual == context.expected,
                  type(context.actual) == type(context.expected),
                  correct_multiplication_used
                  ]
        correct = all(checks)
        actual = context.actual
        if correct:
            mymessages.append(Message(f"Goed zo! Je hebt de computer {repr(context.expected)} laten berekenen."))
        else:
            if not checks[0]:
                mymessages.append(Message(f"Je mag het getal {repr(context.expected)} niet gebruiken voor de variabele {var}."))
            if not checks[1]:
                mymessages.append(Message(f"De waarde voor {var} is niet wat we verwachtten."))
            if not checks[2]:
                types = {int: "integer (geheel getal)", float: "float (kommagetal)", str: "string (tekst)"}
                mymessages.append(Message(f"{repr(context.expected)} is een {types[type(context.expected)]}. Je moet dus dezelfde datatype gebruiken om dat te krijgen."))
            if not checks[3]:
                mymessages.append(Message(f"Merk op dat {repr(repeated_word)} {repetitions} keer herhaald wordt. Gebruik dus de juiste vermenigvuldiging."))

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(actual),
      messages = mymessages
    )