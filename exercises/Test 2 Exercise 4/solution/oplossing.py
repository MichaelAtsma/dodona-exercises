def InkomstenBelasting(inkomen):
    if inkomen < 10000:
        belasting = inkomen * 0.10
        bericht = f"Je moet 10% belasting betalen. Dat is dus €{belasting}."
    elif inkomen < 50000:
        belasting = inkomen * 0.20
        bericht = f"Je moet 20% belasting betalen. Dat is dus €{belasting}."
    else:
        belasting = inkomen * 0.40
        bericht = f"Je moet 40% belasting betalen. Dat is dus €{belasting}."

    return bericht