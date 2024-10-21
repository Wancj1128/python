
def wjj_range_number():
    wjj_number = []
    for number in range(1,301):
        wjj_number.append(number)
    return wjj_number
def wjj_main():
    number_list = wjj_range_number()
    special_number = []
    for a in range(len(number_list)):
        if number_list[a] % 2 == 0 and number_list[a] % 3 == 0 and number_list[a] % 5 == 0:
            special_number.append(number_list[a])
            a += 1
        else:
            a += 1
    print(special_number)

wjj_main()