import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def PositiefOfNegatief(x):
    if x >= 0:
        tekst = "Dit getal is positief"
    else:
        tekst = "Dit getal is negatief"
    return tekst

# X = [5, -9, 0, -2.4] 
X = range(-100, 101)

result = ""
for args in itertools.product(X):
    result += f">>> PositiefOfNegatief({', '.join(map(str, args))})\n"
    result += f"{repr(PositiefOfNegatief(*args))}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)