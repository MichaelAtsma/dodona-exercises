def SpecialeGetallen(lijst):
    aantal_speciaal = 0
    aantal_andere = 0
    
    for getal in lijst:
        if getal == 2:
            aantal_speciaal = aantal_speciaal + 1
        elif getal == 42:
            aantal_speciaal = aantal_speciaal + 1
        elif getal == 73:
            aantal_speciaal = aantal_speciaal + 1
        elif getal == 1729:
            aantal_speciaal = aantal_speciaal + 1
        elif getal == 6174:
            aantal_speciaal = aantal_speciaal + 1
        else:
            aantal_andere = aantal_andere + 1
            
    print(f"De lijst bevat {aantal_speciaal} speciale getallen en {aantal_andere} andere getallen.")