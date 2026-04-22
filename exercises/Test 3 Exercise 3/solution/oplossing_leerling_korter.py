def IsDeelbaar(n):
    for i in range(n):
        if i <= 1:
            a = 1
        elif n % i == 0:
            return True

    return False