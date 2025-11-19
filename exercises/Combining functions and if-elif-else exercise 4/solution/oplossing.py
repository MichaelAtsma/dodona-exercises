def Prijscategorie(prijs):
    if prijs < 5:
        tekst = "Goedkoop"
    elif prijs <= 15:
        tekst = "Normaal"
    else:
        tekst = "Duur"
    return tekst