def Portemonnee(prijzen, geld_in_portemonnee):
    for prijs in prijzen:
        geld_in_portemonnee = geld_in_portemonnee - prijs
        print(f"Na de aankoop van €{prijs} heeft u nog €{geld_in_portemonnee} over in uw portemonnee.")