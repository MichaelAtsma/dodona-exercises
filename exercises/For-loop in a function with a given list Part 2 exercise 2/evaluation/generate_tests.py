import random
import pyperclip
import itertools

def copy_to_clipboard(text):
    pyperclip.copy(text)

def PrintVoldoendes(scorelijst):
    res = []
    for score in scorelijst:
        if score >= 50:
            res.append(f"{score}% is een voldoende.")
    return "\n".join(res)

function_effect = "prints"
function = PrintVoldoendes
bulk_test = True

if not bulk_test:
    X = [([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],),
         ([49, 50, 51],),
         ([1, 2, 4, 8, 16, 32],),
         ([],)]
else:
    X = [([random.randint(0, 1000)/10 for _ in range(random.randint(1, 20))],) for n in range(100)]
    edge_cases = ([49.9, 49.99, 49.999, 50.0, 50.001, 50.01, 50.1],)
    X.append(edge_cases)

result = ""
for args in X:
    result += f">>> {function.__name__}({', '.join(map(str, args))})\n"
    if function_effect == "returns":
        result += f"{repr(function(*args))}\n"
    else:
        result += f"{function(*args)}\n"
    # if not function(*args):
    #     result = result[:-1]  # Remove last newline if no output

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)