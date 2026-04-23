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

def SomDelers(n):
    som = 0

    for i in range(n):
        deler = i + 1
        if n % deler == 0:
            som = som + deler
            
    return som

def IsPriemEfficient(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def IsPriem(n):
    return IsPriemEfficient(n)
    aantal_delers = 0

    for i in range(n):
        if n % (i+1) == 0:
            aantal_delers = aantal_delers + 1

    if aantal_delers == 2:
        return True
    else:
        return False 

def NextPrime(p):
    while True:
        p += 1
        if IsPriemEfficient(p):
            return p

def GenerateSequentialNonPrimes(n, min_factors=3, max_factors=10, skip_step=0):
    currentPrime = 1
    yielded = 0
    while yielded < n:
        non_prime = 1
        for _ in range(random.randint(min_factors, max_factors)):
            for _ in range(skip_step+1):
                currentPrime = NextPrime(currentPrime)
            currentPrime = NextPrime(currentPrime)
            non_prime *= currentPrime
        yield non_prime
        yielded += 1

def GenerateSequentialPrimes(n, skip_first=0, skip_step=0):
    currentPrime = 1
    for _ in range(skip_first):
        currentPrime = NextPrime(currentPrime)
    for _ in range(n):
        currentPrime = NextPrime(currentPrime)
        yield currentPrime
        for _ in range(skip_step):
            currentPrime = NextPrime(currentPrime)


function_effect = "returns"
function = SomDelers
bulk_test = False

start = time.time()

if not bulk_test:
    X = [(2,),
         (3,),
         (4,),
         (15,),
         (1,),
         (113,)]
else:
    amount = 100
    edge_cases = [(1,), (1_000_000,)]
    n = 1_000_000
    while True:
        if IsPriem(n):
            edge_cases.append((n,))
            break
        n -= 1
    X = edge_cases.copy()
    non_primes = GenerateSequentialNonPrimes(amount//2 + 1, min_factors=2, max_factors=2, skip_step=5)
    primes = GenerateSequentialPrimes(amount//2 + 1, skip_first=5, skip_step=19)
    while len(X) < amount:
        if len(X) % 2 == 0:
            X.append((next(non_primes),))
        else:
            X.append((next(primes),))

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