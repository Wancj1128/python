def f(i):
    b = 0
    for a in range(1,i+1):
        b = a / (a+1)
    return b
i = 2
print("%.2f"%f(i))

