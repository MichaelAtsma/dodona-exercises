def KlasUitslag(geslaagd, totaal):
    percentage = geslaagd / totaal * 100
    if percentage < 50:
        uitslag = "Minder dan de helft van de klas is geslaagd is geslaagd."
    elif percentage <= 80:
        uitslag = "Een voldoende aantal leerlingen is geslaagd voor het examen."
    else:
        uitslag = "Wow, wat een sterke klas zijn jullie!"
    return uitslag