def SomNKwadraten(n):
    totaal = 0
    for i in range(n):
        kwadraat = (i + 1) ** 2
        totaal = totaal + kwadraat
    return totaal