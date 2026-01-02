def EvenOnevenOfKomma(getal):
    if int(getal) != getal:
        return f"{getal} is kommagetal."
    elif getal % 2 == 0:
        return f"{getal} is een even geheel getal."
    else:
        return f"{getal} is een oneven geheel getal."