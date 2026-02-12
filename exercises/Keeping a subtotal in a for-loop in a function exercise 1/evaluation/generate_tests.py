import io
import random
import sys
import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        return_value = func(*args, **kwargs)
        return return_value, sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

def SomVanKwadraten(getallen):
    totaal = 0
    for getal in getallen:
        kwadraat = getal ** 2
        totaal = totaal + kwadraat
    return totaal


function_effect = "returns"
function = SomVanKwadraten
bulk_test = True

if not bulk_test:
    X = [([10, 5, 3],),
         ([1, 2, 4, 8, 16, 32],),
         ([2, 3, 4],),
         ([],),]
else:
    amount = 100
    edge_cases = [([-1, -2, -3],), 
                  ([],)]
    X = [(random.choices(range(-100, 100), k=random.randint(0, 50)),) for _ in range(amount-len(edge_cases))]
    X += edge_cases

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    elif function_effect == "prints":
        _, output = capture_output(function, *args)
        result += f"{output}"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)