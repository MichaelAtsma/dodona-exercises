import random
import pyperclip
import itertools
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

def PrintGroterDan5(getallen):
    for getal in getallen:
        if getal > 5:
            print(f"{getal} is groter dan 5.")

function_effect = "prints"
function = PrintGroterDan5
bulk_test = False

if not bulk_test:
    X = [([3, 7, 2, 9, 4],),
         ([6, 3, -7, 42, -91, 28],), 
        ([1, 2, 4, 8, 16, 32],), 
        ([5, 4, 3, 2, 1, 0],)]
else:
    X = [([random.randint(1, 10000) for _ in range(random.randint(1, 20))],) for n in range(100)]
    edge_cases = [([4.9, 5.0, 5.1, 5.01, 5.0001, 5.00001],),
                  ([],)]
    X += edge_cases

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