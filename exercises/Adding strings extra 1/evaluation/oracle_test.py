from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def evaluate_test(context, var):
    submission = get_submission_code()
    checks = {}
    checks["answer_not_used"] = str(context.expected) not in submission
    checks["correct type"] = (type(context.actual)) == (type(context.expected))
    checks["correct value"] = context.actual == context.expected
    checks["addition used"] = '+' in submission

    mymessages = []
    correct = all(checks.values())
    actual = context.actual
    if correct:
        mymessages.append(Message(f"Goed zo! Je hebt de computer {repr(context.expected)} laten berekenen."))
    else:
        if not checks["answer_not_used"]:
            mymessages.append(Message(f"Je mag de zin {repr(context.expected)} niet gebruiken voor de variabele {var}."))
        if not checks["correct value"]:
            mymessages.append(Message(f"De waarde voor {var} is niet wat we verwachtten."))
        if not checks["correct type"]:
            types = {int: "integer (geheel getal)", float: "float (kommagetal)", str: "string (tekst)"}
            mymessages.append(Message(f"{context.expected} is een {types[type(context.expected)]}. Je moet dus dezelfde datatype gebruiken om dat te krijgen."))
        if not checks["addition used"]:
            mymessages.append(Message(f"Je moet een optelling (+) gebruiken om {var} te berekenen."))

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(actual),
      messages = mymessages
    )