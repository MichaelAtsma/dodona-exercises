import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def EindigtOpVier(n):
    if n % 10 == 4:
        return f"{n} eindigt op een 4."
    else:
        return f"{n} eindigt niet op een 4."

result = "\\n".join([EindigtOpVier(i) for i in range(51)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)