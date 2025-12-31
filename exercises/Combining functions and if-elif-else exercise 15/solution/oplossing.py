def KlasGrootte(aantal_leerlingen):
    if aantal_leerlingen < 0:
        return "Dit is geen valide invoer."
    elif aantal_leerlingen == 0:
        return "De klas is leeg."
    elif aantal_leerlingen <= 15:
        return "Dit is een kleine klas."
    elif aantal_leerlingen <= 20:
        return "Dit is een gemiddelde klas."
    elif aantal_leerlingen <= 24:
        return "Dit is een grote klas."
    else:
        return "Dit zijn te veel leerlingen voor één klas."