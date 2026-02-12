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

def Totaalprijs(prijzen):
    totaal = 0
    for prijs in prijzen:
        totaal = totaal + prijs
    return totaal


function_effect = "returns"
function = Totaalprijs
bulk_test = True

if not bulk_test:
    X = [([10.99, 5.49, 3.50],),
         ([1, 2, 4, 8, 16, 32],),
         ([2.99, 12.50, 7.00, 7.00, -7.00, 5.33],),
         ([],),]
else:
    amount = 100
    edge_cases = [([-1, -2, -3],), 
                  ([],)]
    X = edge_cases.copy()
    while len(X) < amount:
        to_append = [(random.randint(0, 10001)/100)*((random.randint(0, 5)>0)*2-1) for _ in range(random.randint(1, 50))]
        if len(str(Totaalprijs(to_append)).split(".")[1]) <= 2:
            X.append( (to_append,) )

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