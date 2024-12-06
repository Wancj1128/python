def add_number(n):
    x = abs(n)
    s = 0
    for i in str(x):
        s += int(str(i))
    return s

a = 111
print(add_number(a))