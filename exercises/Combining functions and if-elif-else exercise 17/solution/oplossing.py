def FilmDuur(uren, minuten):
    if uren >= 2:
        conclusie = "Lange film."
    elif uren == 0:
        conclusie = "Hele korte film."
    elif minuten < 20:
        conclusie = "Korte film."
    else:
        conclusie = "Normale film."
    
    return conclusie