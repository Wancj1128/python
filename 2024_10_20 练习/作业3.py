scores = []
for i in range(5):
    name = input('请输入学生的姓名: ')
    english = input('请输入此学生的英语分数:')
    python = input('请输入此学生的python分数:')
    math = input('请输入该学生的数学分数:')
    print("-------------------------------")
    student = {'name': name, 'english': english, 'python': python, 'math': math}
    scores.append(student)
print(scores)
for student in scores:
        avg = (int(student['english']) + int(student['python']) + int(student['math']))/3
        student['avg'] = avg
print(scores)
sorted_scores = sorted(scores, key=lambda student: student['avg'], reverse=True)
for students in sorted_scores:
    print(students)
