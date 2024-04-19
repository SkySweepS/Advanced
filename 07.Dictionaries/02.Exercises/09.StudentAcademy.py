n = int(input())
students_grade = {}
individual = {}
count = 0
for i in range(n):
    student = input()
    grade = float(input())
    if student not in students_grade:
        students_grade[student] = grade
        individual[student] = 1
    else:
        students_grade[student] += grade
        individual[student] += 1
for key, value in students_grade.items():
    if key in individual.keys():
        ind = value / individual[key]
        if ind >= 4.50:
            print(f"{key} -> {ind:.2f}")
