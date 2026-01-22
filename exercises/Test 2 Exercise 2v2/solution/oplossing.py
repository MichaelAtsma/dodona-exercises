def RacePrestatie(uur):
    if uur < 1.25:
        wave = "Elite."
    elif uur < 1.75:
        wave = "Wave 1: snelle lopers."
    elif uur < 2.25:
        wave = "Wave 2: gemiddelde lopers."
    else:
        wave = "Wave 3: overige lopers."
    return wave