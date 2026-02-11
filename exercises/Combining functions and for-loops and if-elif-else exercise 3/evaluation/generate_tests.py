import random
import pyperclip
import itertools

from random_word import RandomWords
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

def EvenOnevenOverzicht(aantal):
    for i in range(aantal):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is oneven.")


function = EvenOnevenOverzicht
function_effect = "prints"
bulk_test = False

if not bulk_test:
    X = [4, 11, 0]
else:
    X = range(0, 100)

result = ""
for args in itertools.product(X):
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}"
    elif function_effect == "prints":
        _, output = capture_output(function, *args)
        result += f"{output}"

copy_to_clipboard(result[:-1])  # Remove last newline
print("Copied to clipboard:")
print(result)