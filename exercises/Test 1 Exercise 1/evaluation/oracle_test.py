from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if var in line]

def evaluate_test(context):
    correct = (type(context.actual) == type(context.expected)) and (context.actual == context.expected)

    mymessages = []
    if correct:
        expected = context.expected
    elif type(context.actual) == type(context.expected):
            mymessages = [Message("Je hebt het juiste datatype gebruikt, maar de waarde is incorrect.")]
            expected = context.expected
    else:
        expected = "Omdat dit een toets is wordt het verwachte antwoord hier niet getoond."

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )