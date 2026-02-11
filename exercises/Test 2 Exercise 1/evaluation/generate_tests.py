import pyperclip
import itertools
import random
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

def BoekDikte(aantal_paginas):
    if aantal_paginas < 150:
        bericht = "Dit is een dun boek."
    elif aantal_paginas <= 300:
        bericht = "Dit is een normaal boek."
    else:
        bericht = "Dit is een dik boek."
    return bericht

X = [(90,), (150,), (223,), (300,), (350,)]
X = [(x,) for x in range(5, 401, 5)]

result = ""
for args in X:
    result += f">>> BoekDikte({', '.join(map(repr, args))})\n"
    result += f"{repr(BoekDikte(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
