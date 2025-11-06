import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def MaalTweeOfMinTien(x):
    if x >= 0:
        y = x * 2
    else:
        y = x - 10
    
    return y

X = range(-50, 51)

result = ""
for args in itertools.product(X):
    result += f">>> MaalTweeOfMinTien({', '.join(map(str, args))})\n"
    result += f"{MaalTweeOfMinTien(*args)}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)