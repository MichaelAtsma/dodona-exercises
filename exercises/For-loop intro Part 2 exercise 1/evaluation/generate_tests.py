import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = "\\n".join([f"Dit is herhaling nummer {i}" for i in range(21)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)