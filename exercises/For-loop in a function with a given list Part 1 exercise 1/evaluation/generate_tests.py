import random
import pyperclip
import itertools
import os

def copy_to_clipboard(text):
    pyperclip.copy(text)

def GetGroupsOfAllNames(filename, ordered=True, min_size=3, max_size=7):
    with open(filename, "r", encoding="utf-8") as f:
        student_names_all = [line.strip() for line in f if line.strip()]
        student_names_noduplicates = list(set(student_names_all))
        student_names = sorted(student_names_noduplicates)
    print(f"Loaded {len(student_names)} unique student names.")
    X = []
    while student_names:
        size = random.randint(min_size, max_size)
        if ordered:
            new = student_names[:size]
        else:
            new = random.sample(student_names, k=min(len(student_names), size))
        X.append((new,))
        for name in new:
            student_names.remove(name)
    return X

def VerwelkomIedereen(namen):
    return '\n'.join([f"Welkom {naam}!" for naam in namen])

function_effect = "prints"
function = VerwelkomIedereen
bulk_test = True

if not bulk_test:
    X = [(["Ahmed", "Bryan", "Capucine", "Dani"],),
        (["Elodie", "Fiona", "George"],),
        (["Hiba", "Inès", "Jialue", "Karim", "Lara"],),
        (["Max", "Noemie", "Oscar", "Paulin", "Quirine"],),
        (["Rocco", "Saniya", "Thibault", "Uma", "Victoria"],),
        (["Wided", "Xenophanes", "Yanis", "Zayon"],)]
else:
    X = GetGroupsOfAllNames(os.path.join(os.path.dirname(__file__), "student_names.txt"), ordered=True, min_size=1000, max_size=1000)
    X += GetGroupsOfAllNames(os.path.join(os.path.dirname(__file__), "student_names.txt"), ordered=False, min_size=3, max_size=7)



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