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

def MeesteDeelbareGetallen(getallen1, getallen2, deler):
    deelbaar1 = 0
    deelbaar2 = 0
    
    for getal in getallen1:
        if getal % deler == 0:
            deelbaar1 = deelbaar1 + 1
    
    for getal in getallen2:
        if getal % deler == 0:
            deelbaar2 = deelbaar2 + 1
    
    if deelbaar1 > deelbaar2:
        print(f"De eerste lijst bevat meer getallen deelbaar door {deler}.")
    elif deelbaar2 > deelbaar1:
        print(f"De tweede lijst bevat meer getallen deelbaar door {deler}.")
    else:
        print(f"Beide lijsten bevatten evenveel getallen deelbaar door {deler}.")


function_effect = "prints"
function = MeesteDeelbareGetallen
bulk_test = True

if not bulk_test:
    X = [([6, 9, 10], [15, 19, 20], 3),
         ([20, 21, 22, 23, 24, 25], [10, 15, 50, 100], 5),
         ([4, 35, 26], [12, 11, 10, 9], 2),
         ([], [20], 4)]
else:
    amount = 100
    edge_cases = [([], [], 10),
                  ([5, 9, 11, 101], [1, 2, 3, 4], 1),]
    X = edge_cases.copy()
    while len(X) < amount:
        n_1 = random.randint(1, 50)
        n_2 = random.randint(1, 50)
        numbers1 = [random.randint(0, 10000) for _ in range(n_1)]
        numbers2 = [random.randint(0, 10000) for _ in range(n_2)]
        deler = random.randint(1, 10)
        X.append((numbers1, numbers2, deler))



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