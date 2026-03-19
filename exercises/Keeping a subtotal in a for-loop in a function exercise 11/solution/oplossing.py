def IsPriem(n):
    aantal_delers = 0

    for i in range(n):
        if n % (i+1) == 0:
            aantal_delers = aantal_delers + 1

    if aantal_delers == 2:
        return True
    else:
        return False