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

result = ""
for i in range(1, 10):
    for j in range(10):
        result += f">>> Delen({i}, {j})\n"
        result += f"{j / i}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)