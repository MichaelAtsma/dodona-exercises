def AantalNulwaarden(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        conclusie = "De functie heeft twee verschillende reële nulwaarden."
    elif D == 0:
        conclusie = "De functie heeft precies één reële nulwaarde."
    else:
        conclusie = "De functie heeft geen reële nulwaarden."
    return conclusie