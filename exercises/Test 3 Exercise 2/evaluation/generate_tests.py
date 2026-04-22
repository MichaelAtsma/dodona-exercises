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

def KlinkersEnMedeklinkers(woord):
    klinkers = "aeiou"
    aantal_klinkers = 0
    aantal_medeklinkers = 0
    
    for letter in woord:
        if letter in klinkers:
            aantal_klinkers += 1
        else:
            aantal_medeklinkers += 1
            
    print(f"{woord} bevat {aantal_klinkers} klinkers en {aantal_medeklinkers} medeklinkers.")


def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 50)))

def GenerateRandomStringOrWord():
    forbidden_words = {"bevat", "klinkers", "medeklinkers"} # because of the translation, we don't want these words to appear in the random strings
    if random.randint(0, 3):
        r = RandomWords()
        res = r.get_random_word()
    else:
        res = GenerateRandomString()
    
    if res in forbidden_words:
        return GenerateRandomStringOrWord()
    return res

function_effect = "prints"
function = KlinkersEnMedeklinkers
bulk_test = True

if not bulk_test:
    X = [("voorbeeld",),
         ("michiels",),
         ("atsma",),
         ("ikkanprogrammeren",)]
else:
    amount = 200
    edge_cases = [("",),
                  ("a",),
                  ("b",),
                  ("aeiou",),
                  ("bcdfg",),
                  ("aaaaaaa",),
                  ("eeeeeee",),
                  ("iiiiiii",),
                  ("ooooooo",),
                  ("uuuuuuu",),
                  ("zzzzzzz",),
                  ("aeiouaeiou",),
                  ("bcdfgbcdfg",)]
    X = edge_cases.copy()
    while len(X) < amount:
        word = (GenerateRandomStringOrWord(),)
        if word not in X:
            X.append(word)


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