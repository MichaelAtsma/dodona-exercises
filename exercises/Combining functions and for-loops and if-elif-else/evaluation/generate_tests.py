import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def BegroetVaak(aantal_keer):
    result_lines = ""
    for _ in range(aantal_keer):
        result_lines += "Hallo wereld!\n"
    return result_lines.strip()

function_effect = "prints"
function = BegroetVaak

X = [4, 7, 0]
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