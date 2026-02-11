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

def FilmDuur(uren, minuten):
    if uren >= 2:
        conclusie = "Lange film."
    elif uren == 0:
        conclusie = "Hele korte film."
    elif minuten < 20:
        conclusie = "Korte film."
    else:
        conclusie = "Normale film."
    
    return conclusie

X = [(0, 45), (1, 0), (1, 10), (1, 20), (1, 30), (2, 0), (2, 20)]
Uren = range(0, 2+1)
Minuten = range(0, 59+1)
X = itertools.product(Uren, Minuten)

result = ""
for args in X:
    result += f">>> FilmDuur({', '.join(map(repr, args))})\n"
    result += f"{repr(FilmDuur(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
