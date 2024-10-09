def myZodiac(year):

    zod = \
['猴','鸡','狗','猪','鼠','牛','虎','兔','龙','蛇','马','羊']  #生肖列表
    idx = year % 12
    return zod[idx]
def main():
    y = eval(input("please enter your year of birth:"))
    print("your zodiac sign is:",myZodiac(y))
main()