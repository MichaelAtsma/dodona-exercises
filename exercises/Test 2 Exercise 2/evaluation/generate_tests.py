import pyperclip
import itertools
import random

def copy_to_clipboard(text):
    pyperclip.copy(text)

def DagDeel(uur):
    if uur < 6:
        dag_deel = "Nacht."
    elif uur < 12:
        dag_deel = "Ochtend."
    elif uur < 18:
        dag_deel = "Middag."
    else:
        dag_deel = "Avond."
    return dag_deel

X = [(3,), (6,), (10,), (12,), (15.5,), (18,), (20,)]
X = [(x/10,) for x in range(0, 24*10, 2)]

result = ""
for args in X:
    result += f">>> DagDeel({', '.join(map(repr, args))})\n"
    result += f"{repr(DagDeel(*args))}\n"
copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
