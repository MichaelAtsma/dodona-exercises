def ProductDelers(n):
    product = 1

    for i in range(n):
        deler = i + 1
        if n % deler == 0:
            product = product * deler
            
    print(f"Het product van de delers van {n} is {product}.")