def SomEersteNEven(getallen, n):
    totaal = 0
    aantal = 0
    for getal in getallen:
        if aantal >= n:
            return totaal
        if getal % 2 == 0:
            totaal = totaal + getal
            aantal += 1
    return totaal