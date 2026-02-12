def PrintWachtwoordLengtes(wachtwoorden):
    for wachtwoord in wachtwoorden:
        lengte = len(wachtwoord)
        if lengte == 10:
            print(f"{wachtwoord} is precies lang genoeg als wachtwoord.")
        elif lengte > 10:
            print(f"{wachtwoord} is een lang wachtwoord.")
        else:
            print(f"{wachtwoord} is een te kort wachtwoord.")