def KlinkersEnMedeklinkers(woord):
    klinkers = "aeiou"
    aantal_klinkers = 0
    aantal_medeklinkers = 0
    
    for letter in woord:
        if letter in klinkers:
            aantal_klinkers += 1
        else:
            aantal_medeklinkers += 1
            
    print(f"{woord} bevat {aantal_klinkers} klinkers en {aantal_medeklinkers} medeklinkers.")