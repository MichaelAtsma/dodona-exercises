from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if var in line]

def evaluate_test(context, boilerplate):
    submission = get_submission_code()
    
    checks = []
    mymessages = []

    boilerplateLinesIntact = True
    for line in boilerplate.splitlines():
        if line.strip() not in submission:
            boilerplateLinesIntact = False
            break
    checks.append(boilerplateLinesIntact)
    if not boilerplateLinesIntact:
        mymessages.append(Message("Zorg ervoor dat je de gegeven code niet aanpast. Je mag enkel een '#' toevoegen."))
    
    lastLineStillLastLine = boilerplate.splitlines()[-1].strip() in submission.splitlines()[-1]
    checks.append(lastLineStillLastLine)
    if not lastLineStillLastLine:
        mymessages.append(Message("Je mag niet de volgorde van de regels veranderen."))
    
    allLinesHaveComment = all('#' in line for line in submission.splitlines() if str(context.expected) not in line)
    checks.append(allLinesHaveComment)
    if not allLinesHaveComment:
        mymessages.append(Message("Zorg ervoor dat je commentaar toevoegt aan alle regels behalve de regel die de verwachte uitvoer bevat."))

    valueIsCorrect = context.expected == context.actual
    checks.append(valueIsCorrect)

    correct = all(checks)

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )