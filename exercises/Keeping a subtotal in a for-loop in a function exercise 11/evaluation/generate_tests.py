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

def IsPriem(n):
    aantal_delers = 0

    for i in range(n):
        if n % (i+1) == 0:
            aantal_delers = aantal_delers + 1
            
    if aantal_delers == 2:
        return True
    else:
        return False


function_effect = "returns"
function = IsPriem
bulk_test = False

if not bulk_test:
    X = [(2,),
         (3,),
         (4,),
         (15,),
         (1,),
         (113,)]
else:
    amount = 100
    edge_cases = [(1,), (1_000_000,)]
    n = 1_000_000
    while True:
        if IsPriem(n):
            edge_cases.append((n,))
            break
        n -= 1
    X = edge_cases.copy()
    while len(X) < amount:
        n = random.randint(1, 1000)
        X.append((n,))



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