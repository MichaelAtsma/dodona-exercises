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

def Prijscategorie(prijs):
    if prijs < 5:
        tekst = "Goedkoop"
    elif prijs <= 15:
        tekst = "Normaal"
    else:
        tekst = "Duur"
    return tekst

X = [3, 4.99, 5, 11, 15, 15.01, 20]
X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> Prijscategorie({', '.join(map(str, args))})\n"
    result += f"{repr(Prijscategorie(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
