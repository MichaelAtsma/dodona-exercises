n = int(input("Met welk getal wil je beginnen? "))

x = n
output = f"Collatz-reeks: {n}"
while x != 1:
    if x % 2 == 0:
        x = x//2
    else:
        x = 3*x+1
    output += f", {x}"

print(output)