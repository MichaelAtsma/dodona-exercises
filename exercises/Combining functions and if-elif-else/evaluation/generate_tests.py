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

def PositiefOfNegatief(x):
    if x > 0:
        tekst = "Dit getal is positief"
    elif x < 0:
        tekst = "Dit getal is negatief"
    else:
        tekst = "Dit is het neutrale getal 0"
    return tekst

X = [5,-3,0]
# X = range(-50, 51)

result = ""
for args in itertools.product(X):
    result += f">>> PositiefOfNegatief({', '.join(map(str, args))})\n"
    result += f"{repr(PositiefOfNegatief(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)