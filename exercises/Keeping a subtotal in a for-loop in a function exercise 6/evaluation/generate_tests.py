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

def SomNKwadraten(n):
    totaal = 0
    for i in range(n):
        kwadraat = (i + 1) ** 2
        totaal = totaal + kwadraat
    return totaal

function_effect = "returns"
function = SomNKwadraten
bulk_test = False

if not bulk_test:
    X = [(3,),
         (7,),]
else:
    amount = 100
    X = [(i,) for i in range(1, amount + 1)]



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