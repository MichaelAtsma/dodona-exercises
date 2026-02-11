import re

regex_tomatch = "[\\n \\t]*([a-zA-Z_]+[a-zA-Z0-9_]*)[ ]*=[ ]*\\[[ ]*10\\.99[ ]*,[ ]*5\\.49[ ]*,[ ]*3\\.50[ ]*\\][ \\t]*[\\n]+[\\n \\t]*totaal[ ]*=[ ]*0[\\n \\t]*[\\n]+for[ ]+([a-zA-Z_]+[a-zA-Z0-9_]*)[ ]+in[ ]+\\1[ ]*:[ ]*[\\n \\t]*[ \\t]+(totaal[ ]*(=[ ]*totaal[ ]*\\+|\\+=)[ ]*\\2)[\\n \\t]*[\\n]+print[ ]*\\([ ]*totaal[ ]*\\)[\\n \\t]*"
submission = """prijzen = [10.99, 5.49, 3.50]

totaal = 0
for prijs in prijzen:
    totaal = totaal + prijs

print(totaal)"""

m = re.fullmatch(regex_tomatch, submission)
if m:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
else:
    print("No match")