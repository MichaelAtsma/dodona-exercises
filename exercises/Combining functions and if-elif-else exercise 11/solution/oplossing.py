def LangsteWoord(woord1, woord2):
    len1 = len(woord1)
    len2 = len(woord2)
    if len1 > len2:
        conclusie = f"{woord1} is het langste woord."
    elif len1 < len2:
        conclusie = f"{woord2} is het langste woord."
    else:
        conclusie = f"{woord1} en {woord2} zijn even lang."
        
    return conclusie