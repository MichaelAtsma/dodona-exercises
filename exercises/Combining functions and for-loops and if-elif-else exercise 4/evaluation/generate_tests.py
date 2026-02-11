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

def RegelsSchrijven(aantal, doel):
    for i in range(aantal):
        regel = i+1
        if regel < doel:
            print(f"Regel nummer {doel} is nog niet afgedrukt.")
        elif regel == doel:
            print(f"Dit is regel nummer {doel}.")
        else:
            print(f"Regel nummer {doel} is al afgedrukt.")

function = RegelsSchrijven
function_effect = "prints"
bulk_test = False

if not bulk_test:
    X = [(4, 2), (11, 5), (0, 20)]
else:
    X = [(i, random.randint(1, 2*i)) for i in range(1, 101)]

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}"
    elif function_effect == "prints":
        _, output = capture_output(function, *args)
        result += f"{output}"

copy_to_clipboard(result[:-1])  # Remove last newline
print("Copied to clipboard:")
print(result)