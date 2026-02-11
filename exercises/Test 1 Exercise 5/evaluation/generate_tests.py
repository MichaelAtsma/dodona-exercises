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
n_results = 0
max_range = 10
for j in range(1, max_range+1):
    for i in range(j+1):
        for k in range(1, max_range+1):
            if i/j*k == i*k/j:
                result += f">>> ToetsPunt({i}, {j}, {k})\n"
                result += f"{i*k/j}\n"
                n_results += 1

copy_to_clipboard(result)
print(f"{n_results} copied to clipboard:")
# print(result)