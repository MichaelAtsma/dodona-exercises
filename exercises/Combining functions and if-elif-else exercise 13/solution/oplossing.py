def BatterijStatus(batterijpercentage):
    if batterijpercentage <= 20:
        status = "Waarschuwing: batterij bijna leeg, u moet binnenkort opladen!"
    elif batterijpercentage >= 80:
        status = "Batterij bijna vol!"
    else:
        status = "Batterijstatus is goed."
        
    return status