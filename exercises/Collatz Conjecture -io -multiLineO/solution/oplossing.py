n = int(input("Met welk getal wil je beginnen? "))

print("Collatz-reeks:")
print(n)
while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = 3*n+1
    print(n)