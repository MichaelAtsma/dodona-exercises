def MeesteKarakters(lijst1, lijst2):
    totaal1 = 0
    totaal2 = 0

    for element in lijst1:
        totaal1 = totaal1 + len(element)
        
    for element in lijst2:
        totaal2 = totaal2 + len(element)
    
    if totaal1 > totaal2:
        print("De eerste lijst bevat de meeste karakters.")
    elif totaal2 > totaal1:
        print("De tweede lijst bevat de meeste karakters.")
    else:
        print("Beide lijsten bevatten evenveel karakters.")