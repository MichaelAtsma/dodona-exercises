import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Seizoen(maand):
    if maand in ["December", "Januari", "Februari"]:
        return "Winter"
    elif maand in ["Maart", "April", "Mei"]:
        return "Lente"
    elif maand in ["Juni", "Juli", "Augustus"]:
        return "Zomer"
    elif maand in ["September", "Oktober", "November"]:
        return "Herfst"
    else:
        return "Ongeldige maand"

X = ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November", "December", "Lunaris"]
X = [
    "Aurelius", "Brumara", "Cerulus", "Demeris", "Elenor", "Feyruar", "Glimber",
    "Hespera", "Ivril", "Jorvember", "Kestrel", "Myrtil", "Norvar", "Ociero",
    "Pyrune", "Quillis", "Rosmara", "Soltember", "Thalor", "Umbria", "Vesperis",
    "Wythen", "Xandor", "Yulian", "Zepharis", "Arcton", "Bellune", "Corvella",
    "Dagent", "Eldrim", "Florisca", "Galdon", "Helion", "Iskren", "Jasmir",
    "Kylendar", "Lormont", "Moren", "Nivalis", "Orell", "Paelun", "Quarim",
    "Rivent", "Silaris", "Tormes", "Ulmar", "Valeris", "Wynthal", "Xylander",
    "Zephyria"
]

result = ""
for args in itertools.product(X):
    result += f">>> Seizoen({', '.join(map(repr, args))})\n"
    result += f"{repr(Seizoen(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
