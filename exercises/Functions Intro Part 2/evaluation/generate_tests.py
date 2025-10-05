import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = ""
for i in range(50):
    for j in range(50):
        result += f">>> Optellen({i}, {j})\n"
        result += f"{i + j}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)