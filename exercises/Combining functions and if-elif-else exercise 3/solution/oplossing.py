def Leeftijdgroep(leeftijd):
    if leeftijd >= 18:
        tekst = "Volwassene"
    elif leeftijd < 12:
        tekst = "Kind"
    else:
        tekst = "Tiener"
    return tekst