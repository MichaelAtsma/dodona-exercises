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

def Kleinste(x, y):
    if x < y:
        kleinste = x
    elif x > y:
        kleinste = y
    else:
        kleinste = "De getallen zijn even klein."
    return kleinste

# X = [(5, 8), (1, -20), (100, 7), (9, 9)]
X1 = range(-10, 11)
X2 = range(-10, 11)
X = itertools.product(X1, X2)

result = ""
for args in X:
    result += f">>> Kleinste({', '.join(map(str, args))})\n"
    result += f"{repr(Kleinste(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
