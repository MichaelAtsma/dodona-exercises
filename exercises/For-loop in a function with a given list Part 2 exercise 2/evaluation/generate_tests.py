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

def PrintVoldoendes(scorelijst):
    for score in scorelijst:
        if score >= 50:
            print(f"{score}% is een voldoende.")

function_effect = "prints"
function = PrintVoldoendes
bulk_test = False

if not bulk_test:
    X = [([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],),
         ([49, 50, 51],),
         ([1, 2, 4, 8, 16, 32],),
         ([],)]
else:
    X = [([random.randint(0, 1000)/10 for _ in range(random.randint(1, 20))],) for n in range(100)]
    edge_cases = ([49.9, 49.99, 49.999, 50.0, 50.001, 50.01, 50.1],)
    X.append(edge_cases)

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