import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = ("Hallo wereld!\\n" * 100)[:-2]  # Remove the last \n for correct formatting

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)