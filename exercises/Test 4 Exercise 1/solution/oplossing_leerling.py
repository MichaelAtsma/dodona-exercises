def NummerAnalyse(n, deler):
    # Vergelijk product en som van de cijfers
    som = 0
    product = 1
    for x in str(n):
        som += int(x)
        product *= int(x)
    if product == som:
        print(f"Het product en de som van de cijfers zijn allebei gelijk aan {som}.")
    elif product > som:
        print(f"Het product van de cijfers ({product}) is groter dan de som van de cijfers ({som}).")
    else:
        print(f"Het product van de cijfers ({product}) is kleiner dan de som van de cijfers ({som}).")

    # Deling door de deler
    quotient = n / deler
    rest = n % deler
    if rest == 0:
        print(f"{n} is een veelvoud van {deler}.")
    else:
        print(f"{n} is niet deelbaar door {deler}, het resultaat is ongeveer {quotient:.2f}.")
