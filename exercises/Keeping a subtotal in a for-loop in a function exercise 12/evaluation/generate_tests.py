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

def GrootsteGemeneDeler(a, b):
    grootste_gemene_deler = 1

    for i in range(min(a, b)):
        deler = i + 1
        if (a % deler == 0) and (b % deler == 0):
            grootste_gemene_deler = deler

    return grootste_gemene_deler


function_effect = "returns"
function = GrootsteGemeneDeler
bulk_test = True

if not bulk_test:
    X = [(12, 18),
         (3, 5),
         (4, 6),
         (15, 25),
         (1, 1),
         (84, 126)]
else:
    amount = 100
    edge_cases = [(x, x) for x in random.sample(range(1, 1000), 10)]
    X = edge_cases.copy()
    while len(X) < amount:
        koppel = (random.randint(1, 1000), random.randint(1, 1000))
        if not random.randint(0, 5):
            multiplier = random.randint(2, 100)
            koppel = tuple(x*multiplier for x in koppel)
        X.append(koppel)



result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    elif function_effect == "prints":
        _, output = capture_output(function, *args)
        result += f"{output}"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)