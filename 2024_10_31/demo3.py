from os import lseek

s1 = input("请输入一串字符串：")
counts = {}
chaifen = s1.split()
for i in chaifen:
    counts[i] = counts.get(i, 0) + 1
lst = list(counts.items())
print(lst)
lst.sort(key=lambda x: x[-1], reverse=True)
