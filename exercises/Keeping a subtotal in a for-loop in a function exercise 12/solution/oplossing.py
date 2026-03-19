def GrootsteGemeneDeler(a, b):
    grootste_gemene_deler = 1

    for i in range(min(a, b)):
        deler = i + 1
        if (a % deler == 0) and (b % deler == 0):
            grootste_gemene_deler = deler

    return grootste_gemene_deler