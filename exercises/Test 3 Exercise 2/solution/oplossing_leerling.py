def KlinkersEnMedeklinkers(woord):
    klinkers = 0
    medeklinkers = 0
    
    for letter in woord:
        if letter == "a":
            klinkers = klinkers + 1
        elif letter == "e":
            klinkers = klinkers + 1
        elif letter == "i":
            klinkers = klinkers + 1
        elif letter == "o":
            klinkers = klinkers + 1
        elif letter == "u":
            klinkers = klinkers + 1
        else:
            medeklinkers = medeklinkers + 1
            
    print(f"{woord} bevat {klinkers} klinkers en {medeklinkers} medeklinkers.")