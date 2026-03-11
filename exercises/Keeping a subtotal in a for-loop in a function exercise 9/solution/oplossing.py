def KlasGemiddelde(scores):
    som = 0
    aantal = 0
    for score in scores:
        if 0 <= score <= 10:
            som = som + score
            aantal = aantal + 1
    gemiddelde = som / aantal
    return round(gemiddelde, 1)