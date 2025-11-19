def TemperatuurBeschrijving(temperatuur):
    if temperatuur > 18:
        tekst = "Het is warm buiten."
    elif temperatuur < 10:
        tekst = "Het is koud buiten."
    else:
        tekst = "Het is gemiddeld buiten."
    return tekst