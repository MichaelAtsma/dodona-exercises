import pyperclip
import itertools
import random

def copy_to_clipboard(text):
    pyperclip.copy(text)

def KlasUitslag(geslaagd, totaal):
    percentage = geslaagd / totaal * 100
    if percentage < 50:
        uitslag = "Minder dan de helft van de klas is geslaagd is geslaagd."
    elif percentage <= 80:
        uitslag = "Een voldoende aantal leerlingen is geslaagd voor het examen."
    else:
        uitslag = "Wow, wat een sterke klas zijn jullie!"
    return uitslag

X = [(7, 22), (9, 18), (13, 19), (16, 20), (20, 21)]
X = [(a, b) for b in range(15, 25) for a in range(0, b)]

result = ""
for args in X:
    result += f">>> KlasUitslag({', '.join(map(repr, args))})\n"
    result += f"{repr(KlasUitslag(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
