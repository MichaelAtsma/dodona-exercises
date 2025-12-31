def RegenVoorspelling(mm_regen):
    if mm_regen == 0:
        return "Het blijft droog vandaag."
    elif mm_regen <= 5:
        return "Er wordt vandaag lichte regen verwacht."
    elif mm_regen <= 10:
        return "Er wordt vandaag matige regen verwacht."
    else:
        return "Er wordt vandaag zware regen verwacht."