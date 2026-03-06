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

def SomAlleEven(getallen):
    totaal = 0
    for getal in getallen:
        if getal % 2 == 0:
            totaal = totaal + getal
    return totaal


function_effect = "returns"
function = SomAlleEven
bulk_test = True

if not bulk_test:
    X = [([1, 2, 3, 4, 5, 6],),
         ([10, 9, 1, 4, 7, 101, 79, 50],),
         ([1, 3, 5, 7, 9],),
         ([],)]
else:
    amount = 100
    edge_cases = [([],)]
    X = edge_cases.copy()
    while len(X) < amount:
        n_numbers = random.randint(1, 20)
        numbers = [random.randint(0, 10000) for _ in range(n_numbers)]
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