def PrintDeelbaarheden3(getallen):
    for getal in getallen:
        if getal % 3 == 0:
            print(f"{getal} is deelbaar door 3.")
        else:
            print(f"{getal} is niet deelbaar door 3.")