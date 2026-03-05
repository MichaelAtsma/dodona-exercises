def AantalGeslaagd(scores):
    geslaagd = 0
    for score in scores:
        if score >= 50:
            geslaagd += 1
    if geslaagd == 1:
        print(f"Er is {geslaagd} leerling geslaagd.")
    else:
        print(f"Er zijn {geslaagd} leerlingen geslaagd.")