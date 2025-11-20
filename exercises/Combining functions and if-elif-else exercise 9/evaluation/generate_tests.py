import pyperclip
import itertools
import random
from random_word import RandomWords

def copy_to_clipboard(text):
    pyperclip.copy(text)

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
