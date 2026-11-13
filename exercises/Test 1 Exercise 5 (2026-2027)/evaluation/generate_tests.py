import pyperclip
import io
import sys
import random

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
max_range = 1000
for i in range(2, max_range+1):
    if not random.randint(0,2):
        x = i * random.choice([-1, 1])
        if random.randint(0,1):
            x += round(random.random(), random.randint(1, 7))
        result += f">>> ToestandstekenWissel({x})\n"
        result += f"{-x}\n"
        n_results += 1

copy_to_clipboard(result)
print(f"{n_results} copied to clipboard:")
# print(result)