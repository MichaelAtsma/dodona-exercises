import pyperclip
import itertools
import random
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

def EvenOfOneven(getal):
    if getal <= 0:
        tekst = "Geen positief getal"
    elif getal % 2 == 0:
        tekst = "Even"
    else:
        tekst = "Oneven"
    return tekst

X = [5, 12, -7, 0]
X = range(-50, 201)

result = ""
for args in itertools.product(X):
    result += f">>> EvenOfOneven({', '.join(map(repr, args))})\n"
    result += f"{repr(EvenOfOneven(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
