import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Kleinste(x, y):
    if x < y:
        kleinste = x
    elif x > y:
        kleinste = y
    else:
        kleinste = "De getallen zijn even klein."
    return kleinste

# X = [(5, 8), (1, -20), (100, 7), (9, 9)]
X1 = range(-10, 11)
X2 = range(-10, 11)
X = itertools.product(X1, X2)

result = ""
for args in X:
    result += f">>> Kleinste({', '.join(map(str, args))})\n"
    result += f"{repr(Kleinste(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
