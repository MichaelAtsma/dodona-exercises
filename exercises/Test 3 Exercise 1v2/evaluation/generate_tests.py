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

def Kassa(producten):
    totaal = 0
    aantal_producten = 0

    for prijs in producten:
        if prijs == "nieuwe klant":
            print(f"Deze klant heeft {aantal_producten} producten gekocht voor €{totaal:.2f}")
            totaal = 0
            aantal_producten = 0
        else:
            totaal = totaal + prijs
            aantal_producten = aantal_producten + 1

def GenerateShoppingCart():
    cart = []
    for _ in range(random.randint(0, 25)):
        if random.randint(0, 5):
            cart.append(round(random.uniform(0, 100), 3))
        else:
            cart.append("nieuwe klant")
    if random.randint(0, 1):
        cart.append("nieuwe klant")
    return cart

function_effect = "prints"
function = Kassa
bulk_test = True

if not bulk_test:
    X = [([2, 5, "nieuwe klant"],),
         ([10, 20, 30, "nieuwe klant", 40, 50, "nieuwe klant"],),
         ([1.49, 0.95, "nieuwe klant", 2, "nieuwe klant", 5.11],),
         ([1.234, "nieuwe klant", 6.415],),
         ([],),
         (["nieuwe klant"],),]
else:
    amount = 200
    edge_cases = [([],),
                  (["nieuwe klant"],),
                  (["nieuwe klant", "nieuwe klant"],),
                  ([0, "nieuwe klant"],),
                  (["nieuwe klant", 0],),
                  ([0, "nieuwe klant", 0, "nieuwe klant", 0],),
                  ([5.543, "nieuwe klant", 5.544, "nieuwe klant", 5.545, "nieuwe klant", 5.546, "nieuwe klant", 5.544, 0.001, "nieuwe klant"],),]
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