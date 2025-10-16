from evaluation_utils import EvaluationResult, Message # type: ignore

def get_submission_code():
    with open("../submission/source", 'r') as f:
        return f.read()

def lines_containing_var(text, var):
    return [line for line in text.splitlines() if (f"{var}=" in line or f"{var} =" in line)]

def evaluate_test_type_check(context, display_expected_on_fail):
    correct_type = type(context.actual) == type(context.expected)

    type_names = {int: "geheel getal (integer)", float: "kommagetal (float)", str: "tekst (string)"}
    mymessages = []

    if not correct_type:
        mymessages = [Message(f"Je hebt een {type_names[type(context.actual)]} gebruikt. Je moet een {type_names[type(context.expected)]} gebruiken.")]
    
    correct_value = str(context.actual) == str(context.expected)

    if not correct_value:
        mymessages.append(Message(f"De waarde is niet wat we verwachtten."))
    
    correct = correct_type and correct_value

    if correct:
        display_expected = context.actual
    else:
        display_expected = display_expected_on_fail

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(display_expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )

def evaluate_test(context, result_var, ingredient_vars, mandatory_symbols_and_display_names, forbidden_symbols):
    submission = get_submission_code()
    checks = {}
    checks["expected value not in code"] = str(context.expected) not in submission # disabled because it's allowed to use the string of the expected value here
    checks["correct type"] = (type(context.actual)) == (type(context.expected))
    if type(context.expected) == float:
        checks["correct value"] = abs(context.actual - context.expected) < 0.0000001
    else:
        checks["correct value"] = context.actual == context.expected
    checks["no forbidden symbols"] = not any(str(symbol) in submission for symbol in forbidden_symbols)

    result_var_lines = lines_containing_var(submission, result_var)
    ingredients_used_for_result = dict.fromkeys(ingredient_vars.keys(), 0)
    values_used_count = dict.fromkeys(ingredient_vars.keys(), 0)
    mandatory_symbols_used = {symbol: 0 for symbol in mandatory_symbols_and_display_names.keys()}
    for result_line in result_var_lines:
        for ingredient_var in ingredient_vars.keys():
            if ingredient_var in result_line:
                ingredients_used_for_result[ingredient_var] += 1
            elif str(ingredient_vars[ingredient_var]) in result_line:
                values_used_count[ingredient_var] += 1
        for symbol in mandatory_symbols_and_display_names.keys():
            if symbol == "f\"" or symbol == "f'":
                if "f\"" in result_line or "f'" in result_line:
                    mandatory_symbols_used[symbol] += 1
            elif symbol in result_line:
                mandatory_symbols_used[symbol] += 1

    ingredients_used_correctly = True
    ingredients_not_used_enough = []
    for ingredient, usage in ingredients_used_for_result.items():
        if usage < len(result_var_lines):
            ingredients_used_correctly = False
            ingredients_not_used_enough.append(ingredient)
    checks["ingredients used correctly"] = ingredients_used_correctly

    values_not_used = True
    values_used = []
    for ingredient, usage in values_used_count.items():
        if usage > 0:
            values_not_used = False
            values_used.append(ingredient)
    checks["variables used instead of their values"] = values_not_used

    all_mandatory_symbols_used = True
    mandatory_symbols_not_used_enough = []
    for symbol, usage in mandatory_symbols_used.items():
        if usage < len(result_var_lines):
            all_mandatory_symbols_used = False
            mandatory_symbols_not_used_enough.append(symbol)
    checks["mandatory symbols used"] = all_mandatory_symbols_used

    correct = all(checks.values())
    mymessages = []
    if correct:
        mymessages.append(Message(f"Goed zo! Je hebt de computer {repr(context.expected)} laten berekenen op basis van {' en '.join(ingredient_vars)} in de int functie."))
    else:
        if not checks["expected value not in code"]:
            mymessages.append(Message(f"Je mag de zin {repr(context.expected)} niet gebruiken in je code."))
        if not checks["correct type"]:
            if isinstance(context.expected, float):
                mymessages.append(Message(f"{repr(context.expected)} is een kommagetal (float). Je moet dus kommagetallen gebruiken om dat te krijgen."))
            elif isinstance(context.expected, int):
                mymessages.append(Message(f"{repr(context.expected)} is een geheel getal (integer). Je moet dus gehele getallen gebruiken om dat te krijgen."))
            elif isinstance(context.expected, str):
                mymessages.append(Message(f"{repr(context.expected)} is een tekst (string). Je moet dus strings en/of f-strings gebruiken om dat te krijgen."))
        if not checks["correct value"]:
            mymessages.append(Message("De uitkomst is niet wat we verwachtten."))
        if not checks["no forbidden symbols"]:
            mymessages.append(Message(f"Je hebt {' en '.join([symbol for symbol in forbidden_symbols if symbol in submission])} gebruikt in je code. Dat mag niet."))
        if not checks["ingredients used correctly"]:
            mymessages.append(Message(f"Je hebt {' en '.join(ingredients_not_used_enough)} niet gebruikt om {result_var} te maken."))
        if not checks["variables used instead of their values"]:
            mymessages.append(Message(f"Je hebt de waarde van {' en '.join(values_used)} letterlijk overgenomen in je code om {result_var} te berekenen. Dat mag niet. Gebruik de variabele(n) {' en '.join(ingredient_vars)} om tot het juiste resultaat te komen."))
        if not checks["mandatory symbols used"]:
            mymessages.append(Message(f"Je moet een {' en '.join([mandatory_symbols_and_display_names[symbol] for symbol in mandatory_symbols_not_used_enough])} gebruiken om {result_var} te maken."))

    return EvaluationResult(
      result = correct,
      dsl_expected = repr(context.expected),
      dsl_actual = repr(context.actual),
      messages = mymessages
    )