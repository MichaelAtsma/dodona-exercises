n = int(input("Which number do you want to start with? "))

x = n
output = f"Collatz-sequence: {n}"
while x != 1:
    if x % 2 == 0:
        x = x//2
    else:
        x = 3*x+1
    output += f", {x}"

print(output)