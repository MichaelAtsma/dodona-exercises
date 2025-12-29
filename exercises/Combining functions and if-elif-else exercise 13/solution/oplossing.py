def BatterijStatus(batterijpercentage):
    if batterijpercentage < 20:
        return "Waarschuwing: batterij bijna leeg, u moet binnenkort opladen!"
    elif batterijpercentage > 80:
        return "Batterij bijna vol!"
    else:
        return "Batterijstatus is goed."