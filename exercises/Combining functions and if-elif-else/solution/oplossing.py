def PositiefOfNegatief(x):
    if x > 0:
        tekst = "Dit getal is positief"
    elif x < 0:
        tekst = "Dit getal is negatief"
    else:
        tekst = "Dit is het neutrale getal 0"
    return tekst