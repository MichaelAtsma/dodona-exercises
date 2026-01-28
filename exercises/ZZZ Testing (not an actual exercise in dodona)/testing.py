import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = ""
for i in range(51):
    if i % 10 == 4:
        result += f"print('{i} eindigt op een 4')\n"
    else:
        result += f"print('{i} eindigt niet op een 4')\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)