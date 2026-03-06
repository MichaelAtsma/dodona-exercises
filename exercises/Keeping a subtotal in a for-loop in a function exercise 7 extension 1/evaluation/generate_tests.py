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

def SomEersteNEven(getallen, n):
    totaal = 0
    aantal = 0
    for getal in getallen:
        if aantal >= n:
            return totaal
        if getal % 2 == 0:
            totaal = totaal + getal
            aantal += 1
    return totaal

def NumberOfEven(getallen):
    aantal = 0
    for getal in getallen:
        if getal % 2 == 0:
            aantal = aantal + 1
    return aantal


function_effect = "returns"
function = SomEersteNEven
bulk_test = True

if not bulk_test:
    X = [([5, 6, 7, 8, 9, 10], 2),
         ([10, 9, 1, 4, 7, 101, 78, 50], 3),
         ([1, 3, 5, 7, 9], 2),
         ([], 10),
         ([1, 2, 3, 4], 5)]
else:
    amount = 100
    edge_cases = [([], 10),
                  ([5, 9, 11, 101], 1),
                  ([1, 2, 3, 4, 5, 6], 0)]
    X = edge_cases.copy()
    while len(X) < amount:
        n_numbers = random.randint(1, 50)
        numbers = [random.randint(0, 10000) for _ in range(n_numbers)]
        if random.randint(0,1):
            X.append((numbers, random.randint(0, NumberOfEven(numbers))))
        else:
            X.append((numbers, random.randint(NumberOfEven(numbers)+1, NumberOfEven(numbers)*3+1)))



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