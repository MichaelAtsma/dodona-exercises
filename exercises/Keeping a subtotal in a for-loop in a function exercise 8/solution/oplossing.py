def MeesteDeelbareGetallen(getallen1, getallen2, deler):
    deelbaar1 = 0
    deelbaar2 = 0
    
    for getal in getallen1:
        if getal % deler == 0:
            deelbaar1 = deelbaar1 + 1
    
    for getal in getallen2:
        if getal % deler == 0:
            deelbaar2 = deelbaar2 + 1
    
    if deelbaar1 > deelbaar2:
        print(f"De eerste lijst bevat meer getallen deelbaar door {deler}.")
    elif deelbaar2 > deelbaar1:
        print(f"De tweede lijst bevat meer getallen deelbaar door {deler}.")
    else:
        print(f"Beide lijsten bevatten evenveel getallen deelbaar door {deler}.")