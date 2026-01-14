def WedstrijdUitslag(scoreA, scoreB, teamA, teamB):
    if scoreA > scoreB:
        uitslag = f"{teamA} heeft gewonnen!"
    elif scoreB > scoreA:
        uitslag = f"{teamB} heeft gewonnen!"
    else:
        uitslag = "Gelijkspel!"
    return uitslag