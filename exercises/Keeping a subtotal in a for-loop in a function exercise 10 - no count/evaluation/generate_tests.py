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


X_example = [("ACGTACGT",),
             ("ACAACAGT",),
             ("AATTACA",),
             ("",),]

amount = 100
edge_cases = [("",), 
              ("A",), 
              ("C",), 
              ("G",), 
              ("T",), 
              ("ACGT",), 
              ("AAAACCCCGGGGTTTT",)]
X_bulk = edge_cases.copy()
while len(X_bulk) < amount-1:
    n = random.randint(1, 100)
    letters = random.choices("ACGT", k=n)
    X_bulk.append(("".join(letters),))
X_bulk.append(("".join(random.choices("ACGT", k=1_000_000)),))



result = """- tab: "Test"
  contexts:
    - testcases:\n"""
for args in X_example:
    if function_effect == "returns":
        result += f"        - expression: \"{function.__name__}({', '.join(map(repr, args))})\"\n"
        result += f"          return: !oracle\n"
        result += f"            oracle: \"custom_check\"\n"
        result += f"            value: {repr(function(*args))}\n"
        result += f"            file: \"oracle_test.py\"\n"
        result += f"            name: \"evaluate_test\"\n"
        result += f"            arguments: [{{\"count\": \"de count functie\"}}]\n"


result += """- tab: "Bulk test"
  contexts:
    - testcases:\n"""
for args in X_bulk:
    if function_effect == "returns":
        result += f"        - expression: \"{function.__name__}({', '.join(map(repr, args))})\"\n"
        result += f"          return: !oracle\n"
        result += f"            oracle: \"custom_check\"\n"
        result += f"            value: {repr(function(*args))}\n"
        result += f"            file: \"oracle_test.py\"\n"
        result += f"            name: \"evaluate_test\"\n"
        result += f"            arguments: [{{\"count\": \"de count functie\"}}]\n"

    # elif function_effect == "prints":
    #     _, output = capture_output(function, *args)
    #     result += f"{output}"
    # figure this out another time, don't feel like it now and I don't need it here.

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)