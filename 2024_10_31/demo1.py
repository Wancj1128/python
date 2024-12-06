from math import sqrt
x = 0
while True:
    x+=1
    y = x + 100
    z = x + 168
    y = sqrt(y)
    z = sqrt(z)
    if (y == int(y)) and (z == int(z)):
        print(x)
        break
