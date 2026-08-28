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

def Interproduct(n):
    product = 1
    for x in str(n):
        product = product * int(x)
    return product

def Intersom(n):
    sum = 0
    for x in str(n):
        sum = sum + int(x)
    return sum

def VergelijkInter(n):
    if Interproduct(n) == Intersom(n):
        print(f"Het product en de som van de cijfers zijn allebei gelijk aan {Interproduct(n)}.")
    elif Interproduct(n) > Intersom(n):
        print(f"Het product van de cijfers ({Interproduct(n)}) is groter dan de som van de cijfers ({Intersom(n)}).")
    else:
        print(f"Het product van de cijfers ({Interproduct(n)}) is kleiner dan de som van de cijfers ({Intersom(n)}).")

def Deling(n, deler):
    if n % deler == 0:
        print(f"{n} is een veelvoud van {deler}.")
    else:
        print(f"{n} is niet deelbaar door {deler}, het resultaat is ongeveer {n/deler:.2f}.")

def NummerAnalyse(n, deler):
    VergelijkInter(n)
    Deling(n, deler)

def FindOneNumberWithEqualProductAndSum(digits, start_search_digit=2, starttime=None, timeout=5):
    # Made to find the same number every time for a set number of digits, solely to get numbers with many digits.
    if starttime is None:
        starttime = time.time()
    def search(product, total, count, digits_found, start_digit=start_search_digit, starttime=starttime, timeout=timeout):
        if time.time() - starttime > timeout:
            raise TimeoutError("Search timed out after {} seconds".format(timeout))
        current_d = product - total + count

        if current_d == digits:
            return digits_found

        if current_d > digits:
            return None

        for digit in range(start_digit, 10):
            result = search(
                product * digit,
                total + digit,
                count + 1,
                digits_found + [digit],
                start_digit=digit,
                starttime=starttime,
                timeout=timeout
            )

            if result is not None:
                return result

        return None

    nonone_digits = search(1, 0, 0, [], start_digit=start_search_digit, starttime=starttime, timeout=timeout)

    if nonone_digits:
        return int("".join([str(dig) for dig in nonone_digits]) + "1"*(digits-len(nonone_digits)))
    return None

def make_big_dict(total_timeout=5, digit_timeout=5, min_digits=1, max_digits=4300):
    total_start_time = time.time()
    big_dict = {}
    digits = min_digits
    while time.time() - total_start_time < total_timeout and digits <= max_digits:
        digit_start_time = time.time()
        big_dict[digits] = {}
        for start_digit in range(2, 10):
            try:
                number = FindOneNumberWithEqualProductAndSum(digits, start_search_digit=start_digit, starttime=digit_start_time, timeout=digit_timeout)
                if number:
                    big_dict[digits][start_digit] = number
            except TimeoutError:
                print(f"Timeout reached for {digits} digits with start digit {start_digit}. Stopping search for this digit.")
                break
        if big_dict[digits] == {}:
            del big_dict[digits]
        digits += 1
    return big_dict, time.time() - total_start_time


def GenerateTestCase(digits, prod_som_gelijk=False, big_dict={}):
    if prod_som_gelijk:
        if digits in big_dict and big_dict[digits]:
            start_digit = random.choice(list(big_dict[digits].keys()))
            n = big_dict[digits][start_digit]
            del big_dict[digits][start_digit]
            # if random.choice([True] + [False]*3):  # 25% chance to reverse the number for variety
            #     n = int(str(n)[::-1])  # Reverse the number to add variety
        else:
            n = None
    else:
        n = 1
        while Intersom(n) == Interproduct(n):
            n = random.randint(10**(digits-1), 10**digits - 1)
            n = int(str(n).replace("0", str(random.randint(1, 9))))  # Prevent zeros to avoid Interproduct being zero

    deler = random.randint(2, 15)
    return (n, deler)




function_effect = "prints"
function = NummerAnalyse
bulk_test = False

start = time.time()

if not bulk_test:
    X = [(123, 7),
         (456, 2),
         (111112, 3),]
else:
    amount = 100
    edge_cases = []
    X = edge_cases.copy()
    big_dict, elapsed_time = make_big_dict(total_timeout=10, digit_timeout=5, min_digits=1, max_digits=308)
    print(f"Generated big_dict with {sum(len(res) for res in big_dict.values())} numbers with {len(big_dict)} different digit lengths in {elapsed_time:.2f} seconds.")
    while len(X) < amount:
        digits_low_bound = max(1, int(len(X) / amount * 308 * 0.8))
        digits_high_bound = max(2, min(308, int(len(X) / amount * 308 * 1.2)))
        prod_som_gelijk = random.choice([True, False])
        while not any(d in big_dict and big_dict[d] for d in range(digits_low_bound, digits_high_bound + 1)):
            digits_low_bound = max(1, digits_low_bound - 1)
            digits_high_bound = min(308, digits_high_bound + 1)
        digits = random.randint(digits_low_bound, digits_high_bound)
        test_case = GenerateTestCase(digits, prod_som_gelijk=prod_som_gelijk, big_dict=big_dict)
        if test_case[0] is not None:
            X.append(test_case)

middle = time.time()
print(f"Generated {len(X)} test cases in {middle - start:.2f} seconds.")


result = ""
for args in X:
    try:
        result += f">>> {function.__name__}({', '.join(map(repr, args))})\n"
        if function_effect == "returns":
            result += f"{repr(function(*args))}\n"
        elif function_effect == "prints":
            _, output = capture_output(function, *args)
            result += f"{output}"
    except Exception as e:
        print(f"Error while executing {function.__name__}({", ".join([str(arg) for arg in args])}):\n{e}")
        raise e

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)