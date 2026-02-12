import io
import random
import sys
import pyperclip
import itertools
import os

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

def Portemonnee(prijzen, geld_in_portemonnee):
    print(f"U begint met €{geld_in_portemonnee} in uw portemonnee.")
    for prijs in prijzen:
        geld_in_portemonnee = geld_in_portemonnee - prijs
        print(f"Na de aankoop van €{prijs} heeft u nog €{geld_in_portemonnee} over in uw portemonnee.")

def IsValidInput(prijzen, geld_in_portemonnee):
    for prijs in prijzen:
        geld_in_portemonnee = geld_in_portemonnee - prijs
        if prijs < 0 or geld_in_portemonnee < 0:
            return False
        if len(str(geld_in_portemonnee).split(".")[1]) > 2:
            return False
    return True

function_effect = "prints"
function = Portemonnee
bulk_test = True

if not bulk_test:
    X = [([10, 20, 30], 100), 
         ([5, 15, 15, 10, 5], 50), 
         ([7.99, 2.50, 3.75], 20),
         ([], 20),
         ([2.51], 3.51)]
else:
    amount = 100
    edge_cases = [([0], 5), ([], 1)]
    X = edge_cases.copy()
    while len(X) < amount:
        num_prijzen = random.randint(1, 20)
        prijzen = [round(random.uniform(0.01, 100), 2) for _ in range(num_prijzen)]
        geld_in_portemonnee = round(random.uniform(sum(prijzen), sum(prijzen) + 100), 2)
        if IsValidInput(prijzen, geld_in_portemonnee):
            X.append((prijzen, geld_in_portemonnee))



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