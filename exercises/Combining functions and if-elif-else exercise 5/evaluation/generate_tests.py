import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def ToegangMetNaam(naam):
    if naam == "Ali":
        return "Toegang verleend"
    elif naam == "Helena":
        return "Toegang verleend"
    else:
        return "Toegang geweigerd"

X = ["Ali", "Helena", "Jasmina", "Jos", "Ali El Amrani"]
# X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> ToegangMetNaam({', '.join(map(repr, args))})\n"
    result += f"{repr(ToegangMetNaam(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
