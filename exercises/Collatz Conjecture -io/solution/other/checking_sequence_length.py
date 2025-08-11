def Collatz(n, lim=1000):
    x = n
    i = 0
    while i<=1000:
        if x == 1:
            return i
        elif x % 2 == 0:
            x = x/2
        else:
            x = 3*x+1
        i += 1
    return i

hoogste_i = 0
hoogste_n = 1
for n in range(1,26):
    i = Collatz(n)
    if i > 1000:
        print(f"{n} bereikt 1 niet binnen 1000 stappen.")
    else:
        # print(f"{n} bereikt 1 in {i} stappen.")
        if i > hoogste_i:
            hoogste_i = i
            hoogste_n = n
print(f"De traagste n is {hoogste_n}, die 1 pas bereikt na {hoogste_i} stappen.")