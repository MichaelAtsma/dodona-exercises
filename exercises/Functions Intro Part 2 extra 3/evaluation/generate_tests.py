import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

result = ""
for i in range(5):
    for j in range(5):
        for k in range(5):
            result += f">>> SpecialeBewerking({i}, {j}, {k})\n"
            result += f"{(i + j) * k}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)