a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
i = 0
while i < len(a):
    if (i+1) % 5 == 0:
        print(a[i],end='\n')
        i += 1
    else:
        print(a[i],end=' ')
        i += 1

