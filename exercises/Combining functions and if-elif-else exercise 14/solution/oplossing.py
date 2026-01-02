def RegenVoorspelling(mm_regen):
    if mm_regen == 0:
        voorspelling = "Het blijft droog vandaag."
    elif mm_regen <= 5:
        voorspelling = "Er wordt vandaag lichte regen verwacht."
    elif mm_regen <= 10:
        voorspelling = "Er wordt vandaag matige regen verwacht."
    else:
        voorspelling = "Er wordt vandaag zware regen verwacht."
        
    return voorspelling