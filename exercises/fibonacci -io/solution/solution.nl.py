n = int(input("Hoeveelste Fibonacci-getal wil je hebben? "))

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    fmin2 = 1
    fmin1 = 1
    i = 3
    while i <= n:
        fi = fmin2 + fmin1
        fmin2 = fmin1
        fmin1 = fi
        i += 1

    print(fi)