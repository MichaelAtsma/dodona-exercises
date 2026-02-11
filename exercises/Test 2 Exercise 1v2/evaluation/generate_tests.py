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

def BetoogLengte(aantal_woorden):
    if aantal_woorden < 300:
        bericht = "Dit is een kort betoog."
    elif aantal_woorden <= 800:
        bericht = "Dit is een normaal betoog."
    else:
        bericht = "Dit is een lang betoog."
    return bericht

X = [(90,), (300,), (593,), (800,), (1050,)]
# X = [(x,) for x in range(10, 1101, 10)]

result = ""
for args in X:
    result += f">>> BetoogLengte({', '.join(map(repr, args))})\n"
    result += f"{repr(BetoogLengte(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
