import pyperclip
import itertools
from random_word import RandomWords
import random
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

def TeLangeTekst(tekst):
    if len(tekst) > 10:
        bericht = "Deze tekst is te lang"
    else:
        bericht = "Deze tekst is kort genoeg"
    return bericht

def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-_=+[],.<>?', k=random.randint(1, 20)))

def GenerateRandomStringsAndPhrases(n=50):
    for _ in range(n):
        if random.randint(0, 1):
            yield GenerateRandomString()
        else:
            r = RandomWords()
            yield " ".join([r.get_random_word() for _ in range(random.randint(1, 3))])

# X = ["Hallo", "Hallo wereld", "Dodona", "abcdefghij"]
X = GenerateRandomStringsAndPhrases(100)



result = ""
for args in itertools.product(X):
    result += f">>> TeLangeTekst({', '.join(map(repr, args))})\n"
    result += f"{repr(TeLangeTekst(*args))}\n"

copy_to_clipboard(result)
print("Copied to clipboard:")
print(result)
