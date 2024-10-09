#draw.py
import turtle
t = turtle.Pen()        #创建一支画笔，注意“P”为大写
iCirclesCount = 30
for x in range(iCirclesCount):      #循环30次
    t.circle(100)
    t.left(360/iCirclesCount)
