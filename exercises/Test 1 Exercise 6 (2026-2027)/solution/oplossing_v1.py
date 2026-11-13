def ReceptOmrekenen(oorspronkelijk_gram, oorspronkelijk_personen, nieuw_personen):
    nieuw_gram = oorspronkelijk_gram * nieuw_personen / oorspronkelijk_personen
    # of: nieuw_gram = (oorspronkelijk_gram / oorspronkelijk_personen) * nieuw_personen
    # of: nieuw_gram = (nieuw_personen / oorspronkelijk_personen) * oorspronkelijk_gram
    # De tests worden enkel gedaan met die getallen waarbij deze drie uitdrukkingen gelijk zijn.
    return nieuw_gram