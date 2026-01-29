import random
import pyperclip
import itertools

from random_word import RandomWords

def copy_to_clipboard(text):
    pyperclip.copy(text)

def EvenOnevenOverzicht(aantal):
    result = ""
    for i in range(aantal):
        if i % 2 == 0:
            result += f"{i} is even.\n"
        else:
            result += f"{i} is oneven.\n"
    return result


function = EvenOnevenOverzicht
function_effect = "prints"

X = [4, 11, 0]
X = range(0, 100)

result = ""
for args in itertools.product(X):
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}"
    else:
        result += f"{function(*args)}"

copy_to_clipboard(result[:-1])  # Remove last newline
print("Copied to clipboard:")
print(result)