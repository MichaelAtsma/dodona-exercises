def TeLangeTekst(tekst):
    if len(tekst) > 10:
        bericht = "Deze tekst is te lang"
    else:
        bericht = "Deze tekst is kort genoeg"
    return bericht