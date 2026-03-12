import io
import random
import sys
import pyperclip
import itertools
import os

from random_word import RandomWords

def copy_to_clipboard(text):
    pyperclip.copy(text)

def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        return_value = func(*args, **kwargs)
        return return_value, sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def KlasGemiddelde(scores):
    som = 0
    aantal = 0
    for score in scores:
        if 0 <= score <= 10:
            som = som + score
            aantal = aantal + 1
    gemiddelde = som / aantal
    return round(gemiddelde, 1)


function_effect = "returns"
function = KlasGemiddelde
bulk_test = False

if not bulk_test:
    X = [([6, 9, 10],),
         ([0, 7, -1],),
         ([8, 10, 12, 8, 9, 10, 11],),]
else:
    amount = 100
    edge_cases = [([0],),
                  ([-0.0001, 0.05],),
                  ([10.0001, 5.0499],),]
    X = edge_cases.copy()
    while len(X) < amount:
        n = random.randint(1, 50)
        numbers = [0]*n
        certain_valid_index = random.randint(0, n-1)
        for i in range(n):
            if i == certain_valid_index:
                score_type = "valid_int"
            else:
                score_type = random.choices(["valid_int", "valid_float", "invalid_int_high", "invalid_int_low", "invalid_float_high", "invalid_float_low"], weights=[8, 4, 1, 1, 1, 1], k=1)[0]
            match score_type:
                case "valid_int":
                    numbers[i] = random.randint(0, 10)
                case "valid_float":
                    numbers[i] = round(random.uniform(0, 10), random.randint(1, 6))
                case "invalid_int_high":
                    numbers[i] = random.randint(11, 100)
                case "invalid_int_low":
                    numbers[i] = random.randint(-100, -1)
                case "invalid_float_high":
                    numbers[i] = round(random.uniform(11, 100), random.randint(1, 6))
                case "invalid_float_low":
                    numbers[i] = round(random.uniform(-100, -1), random.randint(1, 6))
        X.append((numbers,))



result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    elif function_effect == "prints":
        _, output = capture_output(function, *args)
        result += f"{output}"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)