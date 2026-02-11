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

def Leeftijdsgroep(leeftijd):
    if leeftijd >= 18:
        tekst = "Volwassene"
    elif leeftijd < 12:
        tekst = "Kind"
    else:
        tekst = "Tiener"
    return tekst

X = [5, 11.5, 12, 12.5, 15, 17.5, 18, 20]
X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> Leeftijdsgroep({', '.join(map(str, args))})\n"
    result += f"{repr(Leeftijdsgroep(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
