def SterkWachtwoord(wachtwoord):
    lengte = len(wachtwoord)
    if lengte < 8:
        return "Wachtwoord te kort"
    elif lengte == 8:
        return "Wachtwoord oké"
    else:
        return "Wachtwoord sterk"