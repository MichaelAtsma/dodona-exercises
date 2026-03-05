import io
import random
import sys
import pyperclip
import itertools
import os

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

def AantalGeslaagd(scores):
    geslaagd = 0
    totaal = 0
    for score in scores:
        totaal += 1
        if score >= 50:
            geslaagd += 1
    print(f"{geslaagd} van de {totaal} leerlingen zijn geslaagd.")

function_effect = "prints"
function = AantalGeslaagd
bulk_test = False

if not bulk_test:
    X = [([10, 20, 30, 40, 50, 60, 70],),
         ([49.9, 50.0, 50.1],),
         ([80, 20, 60, 30, 80, 90, 100, 10],),
         ([80],),
         ([40],),
         ([],)]
else:
    amount = 100
    edge_cases = [([49.99, 49.999, 49.9999, 49.99999, 49.999999, 49.9999999],), 
                  ([0],),
                  ([100],),
                  ([],)]
    X = edge_cases.copy()
    while len(X) < amount:
        length = random.randint(0, 20)
        if random.randint(0, 1):
            X.append(([round(random.uniform(0, 100), random.randint(1, 3)) for _ in range(length)],))
        else:
            X.append(([int(random.uniform(0, 100)) for _ in range(length)],))



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