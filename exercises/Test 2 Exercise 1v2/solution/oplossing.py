def BetoogLengte(aantal_woorden):
    if aantal_woorden < 300:
        bericht = "Dit is een kort betoog."
    elif aantal_woorden <= 800:
        bericht = "Dit is een normaal betoog."
    else:
        bericht = "Dit is een lang betoog."
    return bericht