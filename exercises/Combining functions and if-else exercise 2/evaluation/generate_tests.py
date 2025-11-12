import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Kleinste(x, y):
    if x < y:
        kleinste = x
    else:
        kleinste = y
    return kleinste
    
X = range(-10, 11)
Y = range(-10, 11)

result = ""
for args in itertools.product(X, Y):
    result += f">>> Kleinste({', '.join(map(str, args))})\n"
    result += f"{Kleinste(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)