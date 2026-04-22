def AantalKarakters(lijst1, lijst2):
    totaal = 0

    for element in lijst1:
        totaal = totaal + len(element)
        
    for element in lijst2:
        totaal = totaal + len(element)
    
    return totaal