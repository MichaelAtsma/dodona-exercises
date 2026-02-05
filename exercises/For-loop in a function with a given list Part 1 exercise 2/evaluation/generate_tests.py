import random
import pyperclip
import itertools
import os

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Dubbels(getallen):
    return "\n".join([f"Het dubbele van {getal} is {2 * getal}." for getal in getallen])

function_effect = "prints"
function = Dubbels
bulk_test = True

if not bulk_test:
    X = [([5, 3, -7, 42, -91, 28],),
         ([1, 2, 4, 8, 16, 32],),
         ([5, 4, 3, 2, 1, 0],),
         ([],)]
else:
    X = [([random.randint(-100, 100) for _ in range(random.randint(0, 10))],) for _ in range(100)]



result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    else:
        result += f"{function(*args)}\n"
    if not function(*args):
        result = result[:-1]  # Remove last newline if no output

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)