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

def SpecialeGetallen(lijst):
    speciale_getallen = {2, 42, 73, 1729, 6174}
    aantal_speciaal = 0
    aantal_andere = 0
    
    for getal in lijst:
        if getal in speciale_getallen:
            aantal_speciaal += 1
        else:
            aantal_andere += 1
            
    print(f"Aantal speciale getallen: {aantal_speciaal}.\nAantal andere getallen: {aantal_andere}.")

def GenerateTestCase():
    n = random.randint(0, 50)
    test_case = [0] * n
    for i in range(n):
        if random.random() < 0.2:
            test_case[i] = random.choice([2, 42, 73, 1729, 6174])
        else:
            test_case[i] = random.randint(-100000, 100000)
    return (test_case,)


function_effect = "prints"
function = SpecialeGetallen
bulk_test = False

if not bulk_test:
    X = [([2, 42, 73, 1729, 6174],),
         ([73, 1729, -1, 73],),
         ([10, 0],),
         ([],),
         ([100, -22, 6174, 87],)]
else:
    amount = 200
    edge_cases = [([],),
                  ([1],),
                  ([2],),
                  ([42],),
                  ([73],),
                  ([1729],),
                  ([6174],),
                  ([2, 42, 73, 1729, 6174],),
                  ([1, 3, 4, 5],),
                  ([-1, -2, -3],),
                  ([-2, -42, -73, -1729, -6174],),
                  ([2, 2, 2, 2, 2, 2],),
                  ([42, 42, 42, 42],),
                  ([73, 73, 73],),
                  ([1729, 1729],),
                  ([6174, 6174, 6174, 6174],),
                  ([42, 1, 42, 1, 42],),
                  ([2, 42, 73, 1729, 6174] * 10,)]
    X = edge_cases.copy()
    while len(X) < amount:
        new_test_case = GenerateTestCase()
        if new_test_case not in X:
            X.append(new_test_case)


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