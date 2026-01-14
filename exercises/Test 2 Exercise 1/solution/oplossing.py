def BoekDikte(aantal_paginas):
    if aantal_paginas < 150:
        bericht = "Dit is een dun boek."
    elif aantal_paginas <= 300:
        bericht = "Dit is een normaal boek."
    else:
        bericht = "Dit is een dik boek."
    return bericht