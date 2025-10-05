import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = ""
for i in range(1, 10):
    for j in range(10):
        result += f">>> Delen({i}, {j})\n"
        result += f"{j / i}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)