def Kassa(producten):
    totaal = 0
    aantal_producten = 0

    for prijs in producten:
        if prijs == "nieuwe klant":
            print(f"Deze klant heeft {aantal_producten} producten gekocht voor €{totaal:.2f}")
            totaal = 0
            aantal_producten = 0
        else:
            totaal = totaal + prijs
            aantal_producten = aantal_producten + 1