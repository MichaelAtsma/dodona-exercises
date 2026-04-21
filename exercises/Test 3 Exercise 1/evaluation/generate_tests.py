import io
import random
import sys
import pyperclip
import itertools
import os

from random_word import RandomWords

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

def Kassa(winkelmand):
    totaal = 0
    aantal_producten = 0

    for prijs in winkelmand:
        if prijs == "subtotaal":
            print(f"Het subtotaal van de eerste {aantal_producten} producten is €{totaal:.2f}")
        else:
            totaal += prijs
            aantal_producten += 1

    print(f"De totale prijs van de winkelmand is €{totaal:.2f}")

def GenerateShoppingCart():
    cart = []
    for _ in range(random.randint(0, 25)):
        if random.randint(0, 5):
            cart.append(round(random.uniform(0, 100), 3))
        else:
            cart.append("subtotaal")
    return cart

function_effect = "prints"
function = Kassa
bulk_test = True

if not bulk_test:
    X = [([2, 5],),
         ([10, 20, "subtotaal", 30, 40],),
         ([1.49, 0.95, "subtotaal", 2, "subtotaal", 5.11],),
         ([1.234, "subtotaal", 6.413],),
         ([],),
         (["subtotaal"],),]
else:
    amount = 200
    edge_cases = [([],),
                  (["subtotaal"],),
                  (["subtotaal", "subtotaal"],),
                  (["subtotaal"],),
                  (["subtotaal", "subtotaal"],),
                  ([0, "subtotaal"],),
                  (["subtotaal", 0],),
                  ([0, "subtotaal", 0, "subtotaal", 0],),
                  ([5.543, "subtotaal", 0.001, "subtotaal", 0.001, "subtotaal", 0.001, "subtotaal"],),]
    X = edge_cases.copy()
    while len(X) < amount:
        cart = (GenerateShoppingCart(),)
        if cart not in X:
            X.append(cart)


result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    elif function_effect == "prints":
        _, output = capture_output(function, *args)
        result += f"{output}"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)