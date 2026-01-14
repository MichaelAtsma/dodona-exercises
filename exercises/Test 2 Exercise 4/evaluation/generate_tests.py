import pyperclip
import itertools
import random

def copy_to_clipboard(text):
    pyperclip.copy(text)

def InkomstenBelasting(inkomen):
    if inkomen < 10000:
        belasting = inkomen * 0.10
        bericht = f"Je moet 10% belasting betalen. Dat is dus €{belasting}."
    elif inkomen <= 50000:
        belasting = inkomen * 0.20
        bericht = f"Je moet 20% belasting betalen. Dat is dus €{belasting}."
    else:
        belasting = inkomen * 0.40
        bericht = f"Je moet 40% belasting betalen. Dat is dus €{belasting}."
    return bericht

def InkomstenBelastingHelper(inkomen):
    if inkomen < 10000:
        return inkomen * 0.10
    elif inkomen <= 50000:
        return inkomen * 0.20
    else:
        return inkomen * 0.40

def GenerateRandomLookingNumber(x):
    y = x + random.randint(0, 400)+random.randint(0, 99)/100*5
    while "." not in str(InkomstenBelastingHelper(y))[-3:-1]:
        y = x + random.randint(0, 400)+random.randint(0, 99)/100*5
    return y

X = [(5832,), (10000,), (31893,), (50000,), (62530.45,)]
# X = [(GenerateRandomLookingNumber(x),) for x in range(500, 100000, 500)]

result = ""
for args in X:
    result += f">>> InkomstenBelasting({', '.join(map(repr, args))})\n"
    result += f"{repr(InkomstenBelasting(*args))}\n"
copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
