import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def DagType(dag):
    if dag == "Zaterdag":
        dagtype = "Weekend"
    elif dag == "Zondag":
        dagtype = "Weekend"
    else:
        dagtype = "Weekdag"
    return dagtype

X = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag"]
# X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> DagType({', '.join(map(repr, args))})\n"
    result += f"{repr(DagType(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
