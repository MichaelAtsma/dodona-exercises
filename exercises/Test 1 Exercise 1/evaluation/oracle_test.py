from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if var in line]

def evaluate_test_int(context):
    correct = (type(context.actual) == type(context.expected)) and (context.actual == context.expected)

    mymessages = []
    expected = "Omdat dit een toets is wordt het verwachte antwoord hier niet getoond."
    if not correct:
        if type(context.actual) == type(context.expected):
            mymessages += [Message("Je hebt het juiste datatype gebruikt (integer), maar de waarde is incorrect.")]
            expected = context.expected

    return EvaluationResult(
      result = correct,
      dsl_expected = expected,
      dsl_actual = repr(context.actual),
      messages = mymessages
    )

def evaluate_test_float(context):
    correct = (type(context.actual) == type(context.expected)) and (context.actual == context.expected)

    mymessages = []
    expected = "Omdat dit een toets is wordt het verwachte antwoord hier niet getoond."
    if not correct:
        if type(context.actual) == type(context.expected):
            mymessages += [Message("Je hebt het juiste datatype gebruikt (float), maar de waarde is incorrect.")]
            expected = context.expected

    return EvaluationResult(
      result = correct,
      dsl_expected = expected,
      dsl_actual = repr(context.actual),
      messages = mymessages
    )

def evaluate_test_str(context):
    correct = (type(context.actual) == type(context.expected)) and (context.actual == context.expected)

    mymessages = []
    expected = "Omdat dit een toets is wordt het verwachte antwoord hier niet getoond."
    if not correct:
        if type(context.actual) == type(context.expected):
            mymessages += [Message("Je hebt het juiste datatype gebruikt (string), maar de waarde is incorrect.")]
            expected = context.expected

    return EvaluationResult(
      result = correct,
      dsl_expected = expected,
      dsl_actual = repr(context.actual),
      messages = mymessages
    )