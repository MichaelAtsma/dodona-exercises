import random
import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def PrintAllesInDeLijst(de_lijst):
    return '\n'.join(str(element) for element in de_lijst)

function_effect = "prints"
function = PrintAllesInDeLijst

X = [(["appels", "broccoli", "citroenen", "druiven"],), 
     ([9, 2, 18],), 
     ([70, "Voldoende", 40, "Onvoldoende", 100, "Perfect"],)]
X = [([random.randint(1, 10000) for _ in range(random.randint(1, 20))],) for n in range(100)]

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    else:
        result += f"{function(*args)}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)