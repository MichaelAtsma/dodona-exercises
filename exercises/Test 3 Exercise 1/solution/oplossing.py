def Kassa(winkelmand):
    totaal = 0
    aantal_producten = 0

    for prijs in winkelmand:
        if prijs == "subtotaal":
            print(f"Het subtotaal van de eerste {aantal_producten} producten is €{totaal:.2f}")
        else:
            totaal += prijs
            aantal_producten += 1

    print(f"De totale prijs van de winkelmand is €{totaal:.2f}")