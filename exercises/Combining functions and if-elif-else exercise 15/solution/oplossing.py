def KlasGrootte(aantal_leerlingen):
    if aantal_leerlingen < 0:
        conclusie = "Dit is geen valide invoer."
    elif aantal_leerlingen == 0:
        conclusie = "De klas is leeg."
    elif aantal_leerlingen <= 15:
        conclusie = "Dit is een kleine klas."
    elif aantal_leerlingen <= 20:
        conclusie = "Dit is een gemiddelde klas."
    elif aantal_leerlingen <= 24:
        conclusie = "Dit is een grote klas."
    else:
        conclusie = "Dit zijn te veel leerlingen voor één klas."
        
    return conclusie