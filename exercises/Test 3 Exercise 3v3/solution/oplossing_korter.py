def ProductDelers(n):
    product = n

    for deler in range(2, n):
        if n % deler == 0:
            product = product * deler
            
    print(f"Het product van de delers van {n} is {product}.")