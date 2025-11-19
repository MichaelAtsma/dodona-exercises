import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Leeftijdgroep(leeftijd):
    if leeftijd >= 18:
        tekst = "Volwassene"
    elif leeftijd < 12:
        tekst = "Kind"
    else:
        tekst = "Tiener"
    return tekst

X = [5, 11.5, 12, 12.5, 15, 17.5, 18, 20]
X = [i / 10 for i in range(0, 251)]

result = ""
for args in itertools.product(X):
    result += f">>> Leeftijdgroep({', '.join(map(str, args))})\n"
    result += f"{repr(Leeftijdgroep(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
