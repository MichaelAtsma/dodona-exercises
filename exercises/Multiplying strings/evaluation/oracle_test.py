from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def evaluate_test(context):
    submission = get_submission_code()
    checks = [(str(context.expected) not in submission), 
               ("*" in submission),
               ("+" not in submission),
               (type(context.actual)) == (type(context.expected)),
               (context.actual == context.expected)]
    correct = all(checks)
    
    mymessages = []
    if correct:
        mymessages.append(Message(f"Goed zo! Je hebt de computer {repr(context.expected)} laten berekenen."))
    else:
        if not checks[0]:
            mymessages.append(Message(f"Je mag de string {repr(context.expected)} niet gebruiken in je code."))
        if not checks[1]:
            mymessages.append(Message("Je moet een vermenigvuldiging gebruiken."))
        if not checks[2]:
            mymessages.append(Message("Je mag enkel vermenigvuldigingen gebruiken, geen optellingen."))
        if not checks[3]:
            mymessages.append(Message(f"{repr(context.expected)} is een string. Je moet dus zeker een string gebruiken om dat te krijgen."))
        if not checks[4]:
            mymessages.append(Message("De uitkomst is niet wat we verwachtten."))

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )