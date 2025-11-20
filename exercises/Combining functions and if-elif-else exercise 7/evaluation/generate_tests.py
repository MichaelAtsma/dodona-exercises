import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def CijferBeschrijving(behaalde_punten, maximaal_punten):
    percentage = (behaalde_punten / maximaal_punten) * 100
    if percentage < 50:
        return "Onvoldoende"
    elif percentage >= 90:
        return "Uitstekend"
    else:
        return "Voldoende"

X = [(2, 7), (6, 12), (15, 20), (9, 10), (3, 3)]
X1 = [i / 2 for i in range(0, 20*2+1)]
X2 = range(1, 20+1)
X = itertools.product(X1, X2)

result = ""
for args in X:
    if args[1] >= args[0]:  # maximaal_punten must be >= behaalde_punten
        result += f">>> CijferBeschrijving({', '.join(map(repr, args))})\n"
        result += f"{repr(CijferBeschrijving(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
