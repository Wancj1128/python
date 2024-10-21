#请编写一个程序，输入用户的体重（千克）和身高（米），计算显示其BMI值，同时作出解释性评价。
def wjj_main():
        height = eval(input("请输入您的身高:"))
        weight = eval(input("请输入您的体重:"))
        wjj_bmi = weight/height**2
        print("您的身体质量指数为",wjj_bmi)
        if wjj_bmi < 18:
            print("您的身体质量指数显示您超轻")
        elif wjj_bmi >=18 & wjj_bmi < 25:
            print("您的身体质量指数显示您标准")
        elif wjj_bmi >=25 & wjj_bmi < 27:
            print("您的身体质量指数显示您超重")
        elif wjj_bmi >=27:
            print("您的身体质量指标显示您肥胖175")
        return wjj_bmi
wjj_main()
