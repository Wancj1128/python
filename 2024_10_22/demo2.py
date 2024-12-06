def func(x):
    if x<= 1:
        return 1
    return x+func(x-2)

print(func(9))