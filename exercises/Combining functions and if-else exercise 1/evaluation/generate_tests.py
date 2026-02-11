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

def HalverenOfPlusAcht(x):
    if x < 10:
        return x / 2
    else:
        return x + 8
    
X = range(-100, 101)

result = ""
for args in itertools.product(X):
    result += f">>> HalverenOfPlusAcht({', '.join(map(str, args))})\n"
    result += f"{HalverenOfPlusAcht(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)