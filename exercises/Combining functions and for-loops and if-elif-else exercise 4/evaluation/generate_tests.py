import random
import pyperclip
import itertools

from random_word import RandomWords

def copy_to_clipboard(text):
    pyperclip.copy(text)

def RegelsSchrijven(aantal, doel):
    result = ""
    for i in range(aantal):
        regel = i+1
        if regel < doel:
            result += f"Regel nummer {doel} is nog niet afgedrukt.\n"
        elif regel == doel:
            result += f"Dit is regel nummer {doel}.\n"
        else:
            result += f"Regel nummer {doel} is al afgedrukt.\n"
    return result

function = RegelsSchrijven
function_effect = "prints"

X = [(4, 2), (11, 5), (0, 20)]
X = [(i, random.randint(1, 2*i)) for i in range(1, 101)]

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}"
    else:
        result += f"{function(*args)}"

copy_to_clipboard(result[:-1])  # Remove last newline
print("Copied to clipboard:")
print(result)