import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def KlasGrootte(aantal_leerlingen):
    if aantal_leerlingen < 0:
        return "Dit is geen valide invoer."
    elif aantal_leerlingen == 0:
        return "De klas is leeg."
    elif aantal_leerlingen <= 15:
        return "Dit is een kleine klas."
    elif aantal_leerlingen <= 20:
        return "Dit is een gemiddelde klas."
    elif aantal_leerlingen <= 24:
        return "Dit is een grote klas."
    else:
        return "Dit zijn te veel leerlingen voor één klas."

X = [-5, 0, 5, 15, 18, 21, 27]
X = range(-20, 31)

result = ""
for args in itertools.product(X, repeat=1):
    result += f">>> KlasGrootte({', '.join(map(repr, args))})\n"
    result += f"{repr(KlasGrootte(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
