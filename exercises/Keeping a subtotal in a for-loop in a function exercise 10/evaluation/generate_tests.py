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

def DnaFrequentie(dna_streng):
    A = 0
    C = 0
    G = 0
    T = 0

    for nucleotide in dna_streng:
        if nucleotide == "A":
            A = A + 1
        elif nucleotide == "C":
            C = C + 1
        elif nucleotide == "G":
            G = G + 1
        elif nucleotide == "T":
            T = T + 1
    
    return [A, C, G, T]


function_effect = "returns"
function = DnaFrequentie
bulk_test = True

if not bulk_test:
    X = [("ACGTACGT",),
         ("ACAACAGT",),
         ("AATTACA",),
         ("",),]
else:
    amount = 100
    edge_cases = [("",), 
                  ("A",), 
                  ("C",), 
                  ("G",), 
                  ("T",), 
                  ("ACGT",), 
                  ("AAAACCCCGGGGTTTT",)]
    X = edge_cases.copy()
    while len(X) < amount-1:
        n = random.randint(1, 100)
        letters = random.choices("ACGT", k=n)
        X.append(("".join(letters),))
    X.append(("".join(random.choices("ACGT", k=1_000_000)),))



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