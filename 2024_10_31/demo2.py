def main():
    mingwen = int(input("请输入一个五位的整数："))
    a = mingwen % 10
    b = mingwen / 10 % 10
    c = mingwen / 100 % 10
    d = mingwen / 1000 % 10
    e = mingwen / 100000 % 10
