# 编程实现：输入三角形边长，求三角形面积。其中面积计算使用用户自定义函数实现，并保留2位小数输出，请写出相应程序
import math

a,b,c = input('请输入三角形三条边长:').split(" ")
a = float(a)
b = float(b)
c = float(c)
def space(a,b,c):
    s = math.sqrt((a+b+c)/2 * (a+b) * (a+c) * (b+c))
    return round(s,2)
if a+b>c and a+c>b and b+c>a:
    print("此三角形的面积为",space(a,b,c))
else:
    print("这三条边不能构成三角形")