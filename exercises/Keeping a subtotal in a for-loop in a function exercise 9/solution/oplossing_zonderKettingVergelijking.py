def KlasGemiddelde(scores):
    som = 0
    aantal = 0
    for score in scores:
        if score < 0:
            aantal = aantal
        elif score > 10:
            aantal = aantal
        else:
            som = som + score
            aantal = aantal + 1
    gemiddelde = som / aantal
    return round(gemiddelde, 1)