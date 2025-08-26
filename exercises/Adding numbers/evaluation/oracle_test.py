from evaluation_utils import EvaluationResult, Message

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def evaluate_test(context):
    submission = get_submission_code()
    checks = [(str(context.expected) not in submission), 
               ("+" in submission),
               (context.actual == context.expected),
               (type(context.actual)) == (type(context.expected))]
    correct = all(checks)
    
    mymessages = []
    if correct:
        mymessages.append(Message("Goed zo! Je hebt de computer 10 laten berekenen."))
    else:
        if not checks[0]:
            mymessages.append(Message("Je mag het getal 10 niet gebruiken in je code."))
        if not checks[1]:
            mymessages.append(Message("Je moet een optelling gebruiken."))
        if not checks[2]:
            mymessages.append(Message("10 is een geheel getal (integer). Je moet dus gehele getallen gebruiken om dat te krijgen."))

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )