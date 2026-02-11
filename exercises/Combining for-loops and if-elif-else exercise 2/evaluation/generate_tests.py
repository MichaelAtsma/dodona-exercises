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

def EindigtOpVier(n):
    if n % 10 == 4:
        return f"{n} eindigt op een 4."
    else:
        return f"{n} eindigt niet op een 4."

result = "\\n".join([EindigtOpVier(i) for i in range(51)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)