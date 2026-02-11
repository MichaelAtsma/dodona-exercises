import random
import pyperclip
import itertools
import io
import sys

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

def PrintAllesInDeLijst(de_lijst):
    for element in de_lijst:
        print(element)

function_effect = "prints"
function = PrintAllesInDeLijst
bulk_test = False

if not bulk_test:
    X = [(["appels", "broccoli", "citroenen", "druiven"],), 
        ([9, 2, 18],), 
        ([70, "Voldoende", 40, "Onvoldoende", 100, "Perfect"],)]
else:
    X = [([random.randint(1, 10000) for _ in range(random.randint(1, 20))],) for n in range(100)]

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