def EvenOnevenOfKomma(getal):
    if int(getal) != getal:
        bericht = f"{getal} is kommagetal."
    elif getal % 2 == 0:
        bericht = f"{getal} is een even geheel getal."
    else:
        bericht = f"{getal} is een oneven geheel getal."
        
    return bericht