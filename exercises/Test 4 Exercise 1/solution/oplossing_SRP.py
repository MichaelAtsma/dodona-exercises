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