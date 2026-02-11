import pyperclip
import itertools
import random
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

def EvenOnevenOfKomma(getal):
    if int(getal) != getal:
        bericht = f"{getal} is kommagetal."
    elif getal % 2 == 0:
        bericht = f"{getal} is een even geheel getal."
    else:
        bericht = f"{getal} is een oneven geheel getal."
        
    return bericht

X = [5, 8, 9.3]
X = [x if random.randint(0, 1) else x + round(random.random(), random.randint(1, 7)) for x in range(11, 101)]

result = ""
for args in itertools.product(X, repeat=1):
    result += f">>> EvenOnevenOfKomma({', '.join(map(repr, args))})\n"
    result += f"{repr(EvenOnevenOfKomma(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
