from collections import Counter

Word_List = ["python","computer","book","happy"]

all = [letter for word in Word_List for letter in word]  #先遍历Word_List得到word列表，再遍历各个word得到字母
count_all = Counter(all)

print(count_all)