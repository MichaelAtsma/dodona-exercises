import io
import random
import sys
import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def capture_output(func, *args, **kwargs):
    """Capture the output of a function call."""
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        func(*args, **kwargs)
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def PrintDeelbaarheden3(getallen):
    for getal in getallen:
        if getal % 3 == 0:
            print(f"{getal} is deelbaar door 3.")
        else:
            print(f"{getal} is niet deelbaar door 3.")

function_effect = "prints"
function = PrintDeelbaarheden3
bulk_test = True

if not bulk_test:
    X = [([1, 2, 3, 4, 5, 6],),
         ([15, 9, 3, 12, 6],),
         ([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],),
         ([],),
         ([8, 17, 4, 29, 101],)]
else:
    X = [([random.randint(0, 1000) for _ in range(random.randint(1, 20))],) for n in range(100)]
    edge_cases = ([],)
    X.append(edge_cases)

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    elif function_effect == "prints":
        result += f"{capture_output(function, *args)}\n"
    
    if not function(*args):
        result = result[:-1]  # Remove last newline if no output

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)