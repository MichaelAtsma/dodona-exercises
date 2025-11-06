import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Grootste(x, y):
    if x >= y:
        grootste = x
    else:
        grootste = y
    
    return grootste

X = range(-10, 11)
Y = range(-10, 11)

result = ""
for args in itertools.product(X, Y):
    result += f">>> Grootste({', '.join(map(str, args))})\n"
    result += f"{Grootste(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)