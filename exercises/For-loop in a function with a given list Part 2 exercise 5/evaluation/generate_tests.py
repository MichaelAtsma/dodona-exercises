import io
import random
import sys
import pyperclip
import itertools

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

def PrintWachtwoordLengtes(wachtwoorden):
    for wachtwoord in wachtwoorden:
        lengte = len(wachtwoord)
        if lengte == 10:
            print(f"{wachtwoord} is precies lang genoeg als wachtwoord.")
        elif lengte > 10:
            print(f"{wachtwoord} is een lang wachtwoord.")
        else:
            print(f"{wachtwoord} is een te kort wachtwoord.")


def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-_=+[],.<>?', k=random.randint(1, 20)))

def GenerateRandomStringsAndPhrases(n=50):
    for _ in range(n):
        if random.randint(0, 1):
            yield GenerateRandomString()
        else:
            r = RandomWords()
            yield " ".join([r.get_random_word() for _ in range(random.randint(1, 2))])

# X = ["Hallo", "Hallo wereld", "Dodona", "abcdefghij"]

function_effect = "prints"
function = PrintWachtwoordLengtes
bulk_test = False

if not bulk_test:
    X = [(["wachtwoord", "ditiseenlangwachtwoord", "ww1234"],),
         (["hellokitty", "bobdebouwer", "supersecurepassword", "hallo", "12345678"],),
         ([],)]
else:
    amount = 100
    edge_cases = [([""],), 
                  ([],)]
    X = [([phrase for phrase in GenerateRandomStringsAndPhrases(random.randint(1, 10))],) for _ in range(amount-len(edge_cases))]
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