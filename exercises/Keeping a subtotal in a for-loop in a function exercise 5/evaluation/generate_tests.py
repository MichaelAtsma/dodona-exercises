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

def LangsteWoord(woorden):
    langste = ""
    for woord in woorden:
        if len(woord) > len(langste):
            langste = woord
    return langste

def ValidateWordList(wordlist):
    if not wordlist:
        return wordlist
    valid_wordlist = [word for word in wordlist]
    longest_length = max(len(word) for word in wordlist) if wordlist else 0
    longest_words = [word for word in wordlist if len(word) == longest_length]
    longest_words.remove(random.choice(longest_words))
    while longest_words:
        valid_wordlist.remove(longest_words.pop())
    return valid_wordlist
    

def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-_=+[],.<>?', k=random.randint(1, 20)))

def GenerateRandomStringsAndPhrases(n=50):
    for _ in range(n):
        if random.randint(0, 1):
            yield GenerateRandomString()
        else:
            r = RandomWords()
            yield r.get_random_word()

function_effect = "returns"
function = LangsteWoord
bulk_test = False

if not bulk_test:
    X = [(["appel", "banaan", "kers"],),
         (["kat", "hond", "aap", "olifant"],),]
else:
    amount = 100
    edge_cases = [([""],)]
    X = edge_cases.copy()
    while len(X) < amount:
        n_words = random.randint(0, 15)
        words = list(GenerateRandomStringsAndPhrases(n_words))
        X.append((ValidateWordList(words),))



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