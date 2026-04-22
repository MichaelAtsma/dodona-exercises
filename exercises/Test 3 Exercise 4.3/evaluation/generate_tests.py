import io
import random
import sys
import pyperclip
import itertools
import os
import time

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

def AantalKarakters(lijst1, lijst2):
    totaal = 0

    for element in lijst1:
        totaal = totaal + len(element)
        
    for element in lijst2:
        totaal = totaal + len(element)
    
    return totaal

def GenerateRandomString(length=None):
    if length is None:
        length = random.randint(1, 20)
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-_=+[],.<>?', k=length))

def GenerateRandomStringsAndPhrases(n=50):
    for _ in range(n):
        if random.randint(0, 1):
            yield GenerateRandomString()
        else:
            r = RandomWords()
            yield r.get_random_word()

def GenerateRandomListsOfPhrases(max_n_phrases=5, max_n_words_per_phrase=4):
    n_phrases = random.randint(1, max_n_phrases)
    phrases = []
    for _ in range(n_phrases):
        n_words = random.randint(1, max_n_words_per_phrase)
        words = list(GenerateRandomStringsAndPhrases(n_words))
        phrase = ' '.join(words)
        phrases.append(phrase)
    return phrases


function_effect = "returns"
function = AantalKarakters
bulk_test = False

start = time.time()

if not bulk_test:
    X = [(["hallo", "wereld!"], ["Ik", "kan", "programmeren"]),
         (["Python is een mooie taal", "programmeren is leuk"], ["informaticawetenschappen is een nuttig vak!!", ""]), 
         (["a", "bcd"], []),]
else:
    amount = 100
    edge_cases = [(["1", ""], []),
                  ([""], []),
                  ([], []),
                  ([" ", " ", " "], []),
                  (["a"*1000], ["b"*2000]),
                  (["!"], []),
                  (["@"], []),
                  (["#"], []),
                  ([], ["$"]),
                  (["%"], []),
                  ([], ["^"]),
                  (["&"], []),
                  ([], ["*"]),
                  (["("], []),
                  ([")"], []),
                  ([], ["_"]),
                  (["-"], []),
                  (["="], []),
                  (["+"], []),
                  ([], ["["]),
                  (["]"], []),
                  ([], ["|"]),
                  ([";"], []),
                  (["'"], []),
                  ([], [","]),
                  (["."], []),
                  (["<"], []),
                  ([], [">"]),
                  (["?"], []),
                  ([], ["`"]),
                  (["~"], []),
                  (["€"], []),
                  (["¡"], []),
                  ([], ["¥"]),
                  (["!@#$%^&*()_+-=[]|;:',.<>?`~€¡¥"],[])]
    X = edge_cases.copy()
    X = []
    while len(X) < amount:
        phrases1 = GenerateRandomListsOfPhrases()
        phrases2 = GenerateRandomListsOfPhrases()
        if not random.randint(0, 2):
            dif = sum([len(phrase) for phrase in phrases1]) - sum([len(phrase) for phrase in phrases2])
            if dif > 0:
                phrases2.append(GenerateRandomString(length=dif))
            elif dif < 0:
                phrases1.append(GenerateRandomString(length=-dif))
        X.append((phrases1, phrases2))

middle = time.time()
print(f"Generated {len(X)} test cases in {middle - start:.2f} seconds.")


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