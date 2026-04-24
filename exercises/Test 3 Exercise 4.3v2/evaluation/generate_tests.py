import io
import random
import sys
import pyperclip
import itertools
import os
import time

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

def SomGeschrevenGetallen(lijst1, lijst2):
    totaal = 0

    for getalstring in lijst1:
        totaal = totaal + int(getalstring)
        
    for getalstring in lijst2:
        totaal = totaal + int(getalstring)
    
    return totaal



function_effect = "returns"
function = SomGeschrevenGetallen
bulk_test = True

start = time.time()

if not bulk_test:
    X = [(["1", "2"], ["3", "4", "5"]),
         (["18", "2"], ["20", "0"]), 
         (["1", "2"], []),]
else:
    amount = 100
    edge_cases = [([], []),
                  (["0"], ["0"]),
                  (["0"], []),
                  ([], ["0"]),
                  (["1"], ["2"]),
                  (["-1"], ["-2"]),
                  (["123456789"], ["987654321"]),
                  (["1", "2", "3"], ["4", "5", "6"]),
                  (["10", "20", "30"], ["40", "50", "60"]),]
    X = edge_cases.copy()
    X = []
    while len(X) < amount:
        list1 = [str(random.randint(0, 1000000)) for _ in range(random.randint(0, 20))]
        list2 = [str(random.randint(0, 1000000)) for _ in range(random.randint(0, 20))]
        X.append((list1, list2))

middle = time.time()
print(f"Generated {len(X)} test cases in {middle - start:.2f} seconds.")


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