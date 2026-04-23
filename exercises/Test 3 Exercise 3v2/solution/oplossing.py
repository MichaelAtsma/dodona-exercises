def SomDelers(n):
    som = 0

    for i in range(n):
        deler = i + 1
        if n % deler == 0:
            som = som + deler
            
    return som