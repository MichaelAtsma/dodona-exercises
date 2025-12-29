def SnelheidsBord(gemeten_snelheid, toegestane_snelheid):
    if gemeten_snelheid > toegestane_snelheid:
        return "U rijdt te snel!"
    elif gemeten_snelheid < toegestane_snelheid:
        return "Dankuwel."
    else:
        return "Rijd voorzichtig alstublieft."