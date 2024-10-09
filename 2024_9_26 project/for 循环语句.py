dumy = ['jack',5,False,3.1415926,'mary',["a","b"]]
for x in dumy:
    print(x)
    print(type(x))  #此句代码用来打印x的类型
print("This Line dose not belong to for loop")

#for循环将dumy列表视为一个集合，集合内有多少元素，循环体（第三和第四行）就重复多少次