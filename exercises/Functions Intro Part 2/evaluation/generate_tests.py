import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = ""
for i in range(5):
    for j in range(5):
        result += f">>> Optellen({i}, {j})\n"
        result += f"{i + j}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)