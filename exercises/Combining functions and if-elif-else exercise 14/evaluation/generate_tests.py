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

def RegenVoorspelling(mm_regen):
    if mm_regen == 0:
        voorspelling = "Het blijft droog vandaag."
    elif mm_regen <= 5:
        voorspelling = "Er wordt vandaag lichte regen verwacht."
    elif mm_regen <= 10:
        voorspelling = "Er wordt vandaag matige regen verwacht."
    else:
        voorspelling = "Er wordt vandaag zware regen verwacht."
        
    return voorspelling

X = [0, 3, 5.1, 8.4, 10, 10.1, 23]
X = [x / 10 for x in range(0, 151)]

result = ""
for args in itertools.product(X, repeat=1):
    result += f">>> RegenVoorspelling({', '.join(map(repr, args))})\n"
    result += f"{repr(RegenVoorspelling(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
