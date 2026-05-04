def SpecialeGetallen(lijst):
    speciale_getallen = {2, 42, 73, 1729, 6174}
    aantal_speciaal = 0
    aantal_andere = 0
    
    for getal in lijst:
        if getal in speciale_getallen:
            aantal_speciaal += 1
        else:
            aantal_andere += 1
            
    print(f"Aantal speciale getallen: {aantal_speciaal}.\nAantal andere getallen: {aantal_andere}.")