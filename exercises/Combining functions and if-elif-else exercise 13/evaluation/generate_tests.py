import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def BatterijStatus(batterijpercentage):
    if batterijpercentage <= 20:
        status = "Waarschuwing: batterij bijna leeg, u moet binnenkort opladen!"
    elif batterijpercentage >= 80:
        status = "Batterij bijna vol!"
    else:
        status = "Batterijstatus is goed."
        
    return status

X = [10, 20, 50, 80, 90]
X = range(1, 101)

result = ""
for args in itertools.product(X, repeat=1):
    result += f">>> BatterijStatus({', '.join(map(repr, args))})\n"
    result += f"{repr(BatterijStatus(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
