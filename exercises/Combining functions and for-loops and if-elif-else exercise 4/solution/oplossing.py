def RegelsSchrijven(aantal, doel):
    for i in range(aantal):
        regel = i+1
        if regel < doel:
            print(f"Regel nummer {doel} is nog niet afgedrukt.")
        elif regel == doel:
            print(f"Dit is regel nummer {doel}.")
        else:
            print(f"Regel nummer {doel} is al afgedrukt.")