import io
import random
import sys
import pyperclip
import itertools

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

def PrintRestdeling(getallen, deler):
    for getal in getallen:
        aantal = getal // deler
        rest = getal % deler
        if rest == 0:
            print(f"{deler} past precies {aantal} keer in {getal}.")
        else:
            print(f"{deler} past {aantal} keer in {getal} en de rest is {rest}.")

function_effect = "prints"
function = PrintRestdeling
bulk_test = True

if not bulk_test:
    X = [([1, 2, 3, 4, 5, 6, 7], 3),
         ([25, 63, 100], 7),
         ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 15),
         ([], 2),
         ([8, 17, 4, 29, 101], 2)]
else:
    amount = 100
    edge_cases = [([],random.randint(2, 100)),
                  (random.sample(range(100), 5), 1)]
    X = [([random.randint(0, 1000) for _ in range(random.randint(1, 20))], random.randint(2, 100)) for n in range(amount-len(edge_cases))]
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