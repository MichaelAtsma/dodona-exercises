import pyperclip
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

def ToetsPrestatie(n):
    if n < 50:
        return f"{n}% is een onvoldoende."
    elif n <= 100:
        return f"{n}% is een voldoende."
    else:
        return f"Je kan geen {n}% scoren."

result = "\\n".join([ToetsPrestatie(i) for i in range(111)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)