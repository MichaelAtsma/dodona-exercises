import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def TemperatuurBeschrijving(temperatuur):
    if temperatuur <= 10:
        return "Het is koud buiten."
    elif temperatuur > 18:
        return "Het is warm buiten."
    else:
        return "Het is gemiddeld buiten."

# X = [5, 10, 15, 18, 20]
X = [i / 10 for i in range(-50, 250)]

result = ""
for args in itertools.product(X):
    result += f">>> TemperatuurBeschrijving({', '.join(map(str, args))})\n"
    result += f"{repr(TemperatuurBeschrijving(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
