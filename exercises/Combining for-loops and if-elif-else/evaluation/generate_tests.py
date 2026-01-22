import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def EvenOfOneven(n):
    if n % 2 == 0:
        return f"{n} is een even getal."
    else:
        return f"{n} is een oneven getal."

result = "\\n".join([EvenOfOneven(i) for i in range(301)])

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)