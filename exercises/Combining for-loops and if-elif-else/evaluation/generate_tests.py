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

def EvenOfOneven(n):
    if n % 2 == 0:
        return f"{n} is een even getal."
    else:
        return f"{n} is een oneven getal."

result = "\\n".join([EvenOfOneven(i) for i in range(301)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)