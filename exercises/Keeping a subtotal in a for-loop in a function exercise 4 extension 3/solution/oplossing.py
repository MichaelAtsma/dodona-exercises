def AantalGeslaagd(scores):
    geslaagd = 0
    totaal = 0
    for score in scores:
        totaal += 1
        if score >= 50:
            geslaagd += 1
    print(f"{geslaagd} van de {totaal} leerlingen zijn geslaagd.")