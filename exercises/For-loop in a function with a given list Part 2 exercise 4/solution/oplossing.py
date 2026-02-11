def PrintRestdeling(getallen, deler):
    for getal in getallen:
        aantal = getal // deler
        rest = getal % deler
        if rest == 0:
            print(f"{deler} past precies {aantal} keer in {getal}.")
        else:
            print(f"{deler} past {aantal} keer in {getal} en de rest is {rest}.")