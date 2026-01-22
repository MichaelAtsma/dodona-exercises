import pyperclip
import itertools
import random

def copy_to_clipboard(text):
    pyperclip.copy(text)

def RacePrestatie(uur):
    if uur < 1.25:
        wave = "Elite."
    elif uur < 1.75:
        wave = "Wave 1: snelle lopers."
    elif uur < 2.25:
        wave = "Wave 2: gemiddelde lopers."
    else:
        wave = "Wave 3: overige lopers."
    return wave

X = [(1,), (1.25,), (1.5,), (1.75,), (2,), (2.25,), (2.5,)]
X = [(x/1000,) for x in range(0, 3*1000, 25)]  # from 0 to 3 hours, step 0.025 hours

result = ""
for args in X:
    result += f">>> RacePrestatie({', '.join(map(repr, args))})\n"
    result += f"{repr(RacePrestatie(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
