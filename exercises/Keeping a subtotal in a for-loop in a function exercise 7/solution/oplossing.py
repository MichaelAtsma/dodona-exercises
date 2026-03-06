def SomAlleEven(getallen):
    totaal = 0
    for getal in getallen:
        if getal % 2 == 0:
            totaal = totaal + getal
    return totaal