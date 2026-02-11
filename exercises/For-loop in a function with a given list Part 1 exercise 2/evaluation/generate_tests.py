import random
import pyperclip
import itertools
import os
import io
import sys

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

def Dubbels(getallen):
    for getal in getallen:
        dubbele = 2 * getal
        print(f"Het dubbele van {getal} is {dubbele}.")

function_effect = "prints"
function = Dubbels
bulk_test = False

if not bulk_test:
    X = [([5, 3, -7, 42, -91, 28],),
         ([1, 2, 4, 8, 16, 32],),
         ([5, 4, 3, 2, 1, 0],),
         ([],)]
else:
    X = [([random.randint(-100, 100) for _ in range(random.randint(0, 10))],) for _ in range(100)]



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