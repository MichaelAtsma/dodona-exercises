def SomGeschrevenGetallen(lijst1, lijst2):
    totaal = 0

    for getalstring in lijst1:
        totaal = totaal + int(getalstring)
        
    for getalstring in lijst2:
        totaal = totaal + int(getalstring)
    
    return totaal