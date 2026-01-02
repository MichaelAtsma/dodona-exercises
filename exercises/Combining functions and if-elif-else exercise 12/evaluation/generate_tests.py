import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def SnelheidsBord(gemeten_snelheid, toegestane_snelheid):
    if gemeten_snelheid > toegestane_snelheid:
        bericht = "U rijdt te snel!"
    elif gemeten_snelheid < toegestane_snelheid:
        bericht = "Dankuwel."
    else:
        bericht = "Rijd voorzichtig alstublieft."
        
    return bericht

XY = [(40, 30), (45, 50), (120, 120)]
XY = itertools.product(range(10, 121, 10), repeat=2)

result = ""
for args in XY:
    result += f">>> SnelheidsBord({', '.join(map(repr, args))})\n"
    result += f"{repr(SnelheidsBord(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
