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

def SchoolMotto(woord):
    gokae_letters = "GOKAE"
    aantal_gokae = 0
    aantal_andere = 0
    
    for letter in woord:
        if letter in gokae_letters:
            aantal_gokae += 1
        else:
            aantal_andere += 1
            
    print(f"{woord} bevat {aantal_gokae} GOKAE letters en {aantal_andere} andere letters.")


def PartialUpcase(s):
    res = ""
    for c in s:
        if c in "GOKAEgokae":
            res += random.choices([c.upper(), c.lower()], k=1, weights=[4, 1])[0]
        else:
            res += random.choice([c.upper(), c.lower()])
    return res

def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzGOKAEGOKAEGOKAE', k=random.randint(1, 50)))

def GenerateRandomStringOrWord():
    forbidden_words = {"bevat", "GOKAE letters", "andere letters"} # because of the translation, we don't want these words to appear in the random strings
    if random.randint(0, 3):
        r = RandomWords()
        res = r.get_random_word()
    else:
        res = GenerateRandomString()
    
    res = PartialUpcase(res)
    
    if res in forbidden_words:
        return GenerateRandomStringOrWord()
    return res

function_effect = "prints"
function = SchoolMotto
bulk_test = True

if not bulk_test:
    X = [("vOorbEelD",),
         ("michiEls",),
         ("AtsmA",),
         ("iKKanprOgrAmmeren",),
         ("GOKAEgokae",)]
else:
    amount = 200
    edge_cases = [("",),
                  ("g",),
                  ("G",),
                  ("gokae",),
                  ("GOKAE",),
                  ("GGGGGG",),
                  ("OOOOOO",),
                  ("KKKKKK",),
                  ("AAAAAA",),
                  ("EEEEEE",),
                  ("gggggg",),
                  ("gokaegokae",),
                  ("GOKAEGOKAE",)]
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