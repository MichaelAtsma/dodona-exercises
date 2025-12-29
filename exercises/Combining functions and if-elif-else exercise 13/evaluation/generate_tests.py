import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def BatterijStatus(batterijpercentage):
    if batterijpercentage < 20:
        return "Waarschuwing: batterij bijna leeg, u moet binnenkort opladen!"
    elif batterijpercentage > 80:
        return "Batterij bijna vol!"
    else:
        return "Batterijstatus is goed."

X = [10, 20, 50, 80, 90]
X = range(1, 101)

result = ""
for args in itertools.product(X, repeat=1):
    result += f">>> BatterijStatus({', '.join(map(repr, args))})\n"
    result += f"{repr(BatterijStatus(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
