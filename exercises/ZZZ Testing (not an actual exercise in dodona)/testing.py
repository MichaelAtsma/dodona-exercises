submission = 'for i in range (111):\n    if i < 50:\n        print (f"{i}% is een onvoldoende.")\n    elif i <= 100:\n        print (f"{i}% is een voldoende.")   \n    else:\n        print(f"Je kan geen {i}% scoren.")\n\n'
submission = r"""for i in range (111):
    if i < 50:
        print (f"{i}% is een onvoldoende.")
    elif i <= 100:
        print (f"{i}% is een voldoende.")

    else:
        print(f"Je kan geen {i}% scoren.")




"""

regmatch = "[\\n \\t]*for [a-zA-Z_]+[a-zA-Z0-9_]* in range[ ]*\\(.+\\):((?:\\n(?:[ \\t]+.*)?)*)\\n*"

import re

m1 = re.match(regmatch, submission)
if m1:
    print("re.match MATCHED")
    print(m1.group(0))
    print("-----")
    print(m1.group(1))
    print("=====")
else:
    print("re.match DID NOT MATCH")

m2 = re.fullmatch(regmatch, submission)
if m2:
    print("re.fullmatch MATCHED")
    print(m2.group(0))
    print("-----")
    print(m2.group(1))
    print("=====")
else:
    print("re.fullmatch DID NOT MATCH")