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

def DagType(dag):
    if dag == "Zaterdag":
        dagtype = "Weekend"
    elif dag == "Zondag":
        dagtype = "Weekend"
    else:
        dagtype = "Weekdag"
    return dagtype

X = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]
# X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> DagType({', '.join(map(repr, args))})\n"
    result += f"{repr(DagType(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
