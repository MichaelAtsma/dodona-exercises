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

def ToegangMetNaam(naam):
    if naam == "Ali":
        return "Toegang verleend"
    elif naam == "Helena":
        return "Toegang verleend"
    else:
        return "Toegang geweigerd"

X = ["Ali", "Helena", "Jasmina", "Jos", "Ali El Amrani"]
# X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> ToegangMetNaam({', '.join(map(repr, args))})\n"
    result += f"{repr(ToegangMetNaam(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
