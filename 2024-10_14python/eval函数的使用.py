s = '3.14+3'
print(s,type(s))
x = eval(s)
print(x,type(x))
#eval函数常与input函数连用用于获取用户输出的数值
age = eval(input('请输入您的年龄'))
print(age,type(age))

height = eval(input('请输入您的身高'))
print(height,type(height))

hello = '北京欢迎您'
eval(hello)
print(hello,type(hello))