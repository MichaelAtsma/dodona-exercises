import pyperclip
import itertools
import random
from random_word import RandomWords
import io
import sys

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

def SterkWachtwoord(wachtwoord):
    lengte = len(wachtwoord)
    if lengte < 8:
        tekst = "Wachtwoord te kort"
    elif lengte == 8:
        tekst = "Wachtwoord oké"
    else:
        tekst = "Wachtwoord sterk"
    return tekst

def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-_=+[],.<>?', k=random.randint(1, 20)))

def GenerateRandomStringsAndPhrases(n=50):
    for _ in range(n):
        if random.randint(0, 1):
            yield GenerateRandomString()
        else:
            r = RandomWords()
            yield " ".join([r.get_random_word() for _ in range(random.randint(1, 3))])

X = ["kort", "precies8", "eenlangwachtwoord"]
X = GenerateRandomStringsAndPhrases(100)

result = ""
for args in itertools.product(X):
    result += f">>> SterkWachtwoord({', '.join(map(repr, args))})\n"
    result += f"{repr(SterkWachtwoord(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
