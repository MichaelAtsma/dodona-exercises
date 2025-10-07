from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if var in line]

def evaluate_test(context, show_no_message_for_these_values=[], show_no_message_if_this_character_in_value=[]):
    correct = (type(context.actual) == type(context.expected)) and (context.actual == context.expected)

    mymessages = []
    if correct:
        expected = context.expected
    elif all(type(context.actual) == type(context.expected), 
             context.actual not in show_no_message_for_these_values, 
             not any(char in str(context.actual) for char in show_no_message_if_this_character_in_value)):
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