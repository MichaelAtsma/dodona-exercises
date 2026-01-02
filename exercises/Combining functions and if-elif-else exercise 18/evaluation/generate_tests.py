import pyperclip
import itertools
import random

def copy_to_clipboard(text):
    pyperclip.copy(text)

def AantalNulwaarden(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        conclusie = "De functie heeft twee verschillende reële nulwaarden."
    elif D == 0:
        conclusie = "De functie heeft precies één reële nulwaarde."
    else:
        conclusie = "De functie heeft geen reële nulwaarden."
    return conclusie

def GenerateQuadraticFunction(numberOfRoots):
    limsA = (-5, 10)
    limsB = (-10, 10)
    limsC = (-10, 20)

    a = random.randint(limsA[0]*10, limsA[1]*10)/10
    if int(a) == a:
        a = int(a)
    if a == 0:
        a = random.randint(1, 10)
    
    if numberOfRoots == 2:
        c = random.randint(limsC[0]*10, limsC[1]*10)/10
        
        if a*c < 0:
            bLowLimit, bHighLimit = limsB
        else:
            bLowLimit = (4*a*c)**0.5
            bHighLimit = max(limsB[1], bLowLimit*2)
        b = random.randint(int(bLowLimit*10), int(bHighLimit*10))/10 * random.choice([-1, 1])
    elif numberOfRoots == 1:
        r = random.randint(int(-limsB[0]*10/2), int(limsB[1]*10/2))/10
        b = -2*a*r
        c = a*r**2
    else:
        c = random.randint(limsC[0]*10, limsC[1]*10)/10
        while c == 0:
            c = random.randint(limsC[0]*10, limsC[1]*10)/10
        if a*c < 0:
            c = -c
        b = random.randint(int(-((4*a*c)**0.5)*10), int(((4*a*c)**0.5)*10))/10

    return (a, b, c)

def CleanNumber(num, epsilon=1e-10):
    for r in range(0, 6):
        if abs(num - round(num, r)) < epsilon:
            num = round(num, r)
    if int(num) == num:
        num = int(num)
    return num

def CleanTestCase(testCase):
    return tuple(CleanNumber(x) for x in testCase)

def GenerateTestCases(numberOfTests):
    testCases = set()
    while len(testCases) < numberOfTests:
        roots = random.randint(0, 2)
        currentLength = len(testCases)
        while len(testCases) == currentLength:
            testCase = GenerateQuadraticFunction(roots)
            testCase = CleanTestCase(testCase)
            testCases.add(testCase)

    return testCases

X = [(1, 2, 3), (2, -12, 18), (3, 10, 7.2)]
X = GenerateTestCases(200)

result = ""
for args in X:
    result += f">>> AantalNulwaarden({', '.join(map(repr, args))})\n"
    result += f"{repr(AantalNulwaarden(*args))}\n"

copy_to_clipboard(result.strip())
print("Copied to clipboard:")
print(result)
