def LangsteWoord(woorden):
    langste = ""
    for woord in woorden:
        if len(woord) > len(langste):
            langste = woord
    return langste