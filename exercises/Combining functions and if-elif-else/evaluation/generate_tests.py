import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def PositiefOfNegatief(x):
    if x > 0:
        tekst = "Dit getal is positief"
    elif x < 0:
        tekst = "Dit getal is negatief"
    else:
        tekst = "Dit is het neutrale getal 0"
    return tekst

# X = [5,-3,0]
X = range(-50, 51)

result = ""
for args in itertools.product(X):
    result += f">>> PositiefOfNegatief({', '.join(map(str, args))})\n"
    result += f"{PositiefOfNegatief(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)