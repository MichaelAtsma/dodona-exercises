a = [35.8, 94.784, 91.2, 30.37, 71.339, 77.514, 53.3, 68.2, 6.4, 77.1, 2.9]

def AantalGeslaagd(scores):
    geslaagd = 0
    totaal = 0
    for score in scores:
        totaal += 1
        if score >= 50:
            geslaagd += 1
        print(f"Score {score}: {geslaagd} van de {totaal} leerlingen zijn geslaagd.")
    print(f"{geslaagd} van de {totaal} leerlingen zijn geslaagd.")

AantalGeslaagd(a)