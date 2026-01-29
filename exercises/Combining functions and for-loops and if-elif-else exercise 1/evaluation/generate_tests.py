import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def PrintTot(n):
    result_lines = ""
    for i in range(n):
        result_lines += f"{i}\n"
    return result_lines.strip()


function = PrintTot
function_effect = "prints"

X = [4, 10, 0]
X = range(0, 100)

result = ""
for args in itertools.product(X):
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    else:
        result += f"{function(*args)}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)