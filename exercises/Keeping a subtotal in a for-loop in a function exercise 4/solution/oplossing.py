def AantalGeslaagd(scores):
    geslaagd = 0
    for score in scores:
        if score >= 50:
            geslaagd += 1
    return geslaagd