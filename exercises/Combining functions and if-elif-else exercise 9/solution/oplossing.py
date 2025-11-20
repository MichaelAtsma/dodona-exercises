def EvenOfOneven(getal):
    if getal <= 0:
        tekst = "Geen positief getal"
    elif getal % 2 == 0:
        tekst = "Even"
    else:
        tekst = "Oneven"
    return tekst