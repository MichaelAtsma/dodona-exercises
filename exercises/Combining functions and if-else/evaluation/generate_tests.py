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

def MaalTweeOfMinTien(x):
    if x >= 0:
        y = x * 2
    else:
        y = x - 10
    
    return y

X = range(-50, 51)

result = ""
for args in itertools.product(X):
    result += f">>> MaalTweeOfMinTien({', '.join(map(str, args))})\n"
    result += f"{MaalTweeOfMinTien(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)