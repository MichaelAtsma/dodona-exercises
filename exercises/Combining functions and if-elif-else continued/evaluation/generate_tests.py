import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Grootste(x, y):
    if x > y:
        grootste = x
    elif x < y:
        grootste = y
    else:
        grootste = "De getallen zijn even groot."
    return grootste

# X = [(5, 8), (1, -20), (100, 7), (9, 9)]
X1 = range(-10, 11)
X2 = range(-10, 11)
X = itertools.product(X1, X2)

result = ""
for args in X:
    result += f">>> Grootste({', '.join(map(str, args))})\n"
    result += f"{repr(Grootste(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
