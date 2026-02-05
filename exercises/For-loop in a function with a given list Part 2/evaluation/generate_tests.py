import random
import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def PrintGroterDan5(getallen):
    res = []
    for element in getallen:
        if element > 5:
            res.append(f"{element} is groter dan 5")
    return "\n".join(res)

function_effect = "prints"
function = PrintGroterDan5
bulk_test = True

if not bulk_test:
    X = [([3, 7, 2, 9, 4],),
         ([6, 3, -7, 42, -91, 28],), 
        ([1, 2, 4, 8, 16, 32],), 
        ([5, 4, 3, 2, 1, 0],)]
else:
    X = [([random.randint(1, 10000) for _ in range(random.randint(1, 20))],) for n in range(100)]
    edge_cases = [([4.9, 5.0, 5.1, 5.01, 5.0001, 5.00001],),
                  ([],)]
    X += edge_cases

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    else:
        result += f"{function(*args)}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)