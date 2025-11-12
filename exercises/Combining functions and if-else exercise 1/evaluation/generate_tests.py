import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def HalverenOfPlusAcht(x):
    if x < 10:
        return x / 2
    else:
        return x + 8
    
X = range(-100, 101)

result = ""
for args in itertools.product(X):
    result += f">>> HalverenOfPlusAcht({', '.join(map(str, args))})\n"
    result += f"{HalverenOfPlusAcht(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)