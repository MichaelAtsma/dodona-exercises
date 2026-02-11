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

def Grootste(x, y):
    if x >= y:
        grootste = x
    else:
        grootste = y
    
    return grootste

X = range(-10, 11)
Y = range(-10, 11)

result = ""
for args in itertools.product(X, Y):
    result += f">>> Grootste({', '.join(map(str, args))})\n"
    result += f"{Grootste(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)