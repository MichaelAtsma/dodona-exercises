import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Seizoen(maand):
    if maand in ["december", "januari", "februari"]:
        return "Winter"
    elif maand in ["maart", "april", "mei"]:
        return "Lente"
    elif maand in ["juni", "juli", "augustus"]:
        return "Zomer"
    elif maand in ["september", "oktober", "november"]:
        return "Herfst"
    else:
        return "Ongeldige maand"

X = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december", "lunaris"]
# X = range(-50, 201)

result = ""
for args in itertools.product(X):
    result += f">>> Seizoen({', '.join(map(repr, args))})\n"
    result += f"{repr(Seizoen(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
