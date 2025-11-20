def CijferBeschrijving(behaalde_punten, maximaal_punten):
    percentage = (behaalde_punten / maximaal_punten) * 100
    if percentage < 50:
        return "Onvoldoende"
    elif percentage >= 90:
        return "Uitstekend"
    else:
        return "Voldoende"