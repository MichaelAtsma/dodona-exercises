import pyperclip
from random_word import RandomWords
import io
import sys

def copy_to_clipboard(text):
    pyperclip.copy(text)

def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        return_value = func(*args, **kwargs)
        return return_value, sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def LangsteWoord(woord1, woord2):
    len1 = len(woord1)
    len2 = len(woord2)
    if len1 > len2:
        conclusie = f"{woord1} is het langste woord."
    elif len1 < len2:
        conclusie = f"{woord2} is het langste woord."
    else:
        conclusie = f"{woord1} en {woord2} zijn even lang."
        
    return conclusie

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
