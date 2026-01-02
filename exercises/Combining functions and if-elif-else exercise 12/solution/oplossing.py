def SnelheidsBord(gemeten_snelheid, toegestane_snelheid):
    if gemeten_snelheid > toegestane_snelheid:
        bericht = "U rijdt te snel!"
    elif gemeten_snelheid < toegestane_snelheid:
        bericht = "Dankuwel."
    else:
        bericht = "Rijd voorzichtig alstublieft."
        
    return bericht