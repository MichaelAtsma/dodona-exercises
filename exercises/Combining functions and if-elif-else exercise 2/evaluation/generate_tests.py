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

def TemperatuurBeschrijving(temperatuur):
    if temperatuur < 10:
        return "Het is koud buiten."
    elif temperatuur > 18:
        return "Het is warm buiten."
    else:
        return "Het is gemiddeld buiten."

X = [5, 10, 15, 18, 20]
# X = [i / 10 for i in range(-50, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> TemperatuurBeschrijving({', '.join(map(str, args))})\n"
    result += f"{repr(TemperatuurBeschrijving(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
