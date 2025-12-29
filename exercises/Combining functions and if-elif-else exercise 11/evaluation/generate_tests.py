import pyperclip
from random_word import RandomWords

def copy_to_clipboard(text):
    pyperclip.copy(text)

def LangsteWoord(woord1, woord2):
    len1 = len(woord1)
    len2 = len(woord2)
    if len1 > len2:
        return f"{woord1} is het langste woord."
    elif len1 < len2:
        return f"{woord2} is het langste woord."
    else:
        return f"{woord1} en {woord2} zijn even lang."

def GenerateRandomWordCouples(n=50):
    for _ in range(n):
        r = RandomWords()
        yield (r.get_random_word(), r.get_random_word())

# XY = [("programmeren", "Python"), ("deur", "octopus"), ("sleutel", "kikkers")]
XY = GenerateRandomWordCouples(100)

result = ""
for args in XY:
    result += f">>> LangsteWoord({', '.join(map(repr, args))})\n"
    result += f"{repr(LangsteWoord(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
