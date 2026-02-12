def Portemonnee(prijzen, geld_in_portemonnee):
    print(f"U begint met €{geld_in_portemonnee} in uw portemonnee.")
    for prijs in prijzen:
        geld_in_portemonnee = geld_in_portemonnee - prijs
        print(f"Na de aankoop van €{prijs} heeft u nog €{geld_in_portemonnee} over in uw portemonnee.")