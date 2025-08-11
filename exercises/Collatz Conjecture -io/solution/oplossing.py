n = int(input("Met welk getal wil je beginnen? "))

x = n
i = 0
gelukt = 0
while i<1000:
    if x == 1:
        print(f"{n} bereikt 1 in {i} stappen.")
        i = 1000
        gelukt = 1
    elif x % 2 == 0:
        x = x/2
    else:
        x = 3*x+1
    i += 1

if gelukt == 0:
    print(f"{n} bereikt 1 niet binnen 1000 stappen.")