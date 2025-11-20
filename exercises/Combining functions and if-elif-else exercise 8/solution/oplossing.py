def SterkWachtwoord(wachtwoord):
    lengte = len(wachtwoord)
    if lengte < 8:
        tekst = "Wachtwoord te kort"
    elif lengte == 8:
        tekst = "Wachtwoord oké"
    else:
        tekst = "Wachtwoord sterk"
    return tekst