import random
import pyperclip
import itertools

from random_word import RandomWords

def copy_to_clipboard(text):
    pyperclip.copy(text)

def Echo(tekst, aantal):
    result = ""
    for _ in range(aantal):
        result += f"{tekst}\n"
    return result

def GenerateRandomString():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()-_=+[],.<>?', k=random.randint(1, 20)))

def GenerateRandomStringsAndPhrases(n=50):
    for _ in range(n):
        if not random.randint(0, 4):
            yield GenerateRandomString()
        else:
            r = RandomWords()
            yield " ".join([r.get_random_word() for _ in range(random.randint(1, 3))])

def GenerateRandomIntegers(n=50, low=0, high=150):
    population = range(low, high)
    weights = [i/3+1 for i in range(high-1, low-1, -1)]
    return random.choices(population, weights=weights, k=n)



function = Echo
function_effect = "prints"

X = [("Hallo wereld!", 4), ("Python is leuk!", 7), ("Ik houd niet van programmeren", 0), ("", 4)]
bulk_test_length = 100
X_strings = GenerateRandomStringsAndPhrases(bulk_test_length)
X_numbers = GenerateRandomIntegers(n=bulk_test_length, low=0, high=150)
X = zip(X_strings, X_numbers)

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}"
    else:
        result += f"{function(*args)}"

copy_to_clipboard(result[:-1])  # Remove last newline
print("Copied to clipboard:")
print(result)