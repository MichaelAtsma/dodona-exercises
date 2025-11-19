def TemperatuurBeschrijving(temperatuur):
    if temperatuur < 10:
        return "Het is koud buiten."
    elif temperatuur > 18:
        return "Het is warm buiten."
    else:
        return "Het is gemiddeld buiten."