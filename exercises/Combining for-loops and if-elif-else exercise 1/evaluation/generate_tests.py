import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def ToetsPrestatie(n):
    if n < 50:
        return f"{n}% is een onvoldoende."
    elif n <= 100:
        return f"{n}% is een voldoende."
    else:
        return f"Je kan geen {n}% scoren."

result = "\\n".join([ToetsPrestatie(i) for i in range(111)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)