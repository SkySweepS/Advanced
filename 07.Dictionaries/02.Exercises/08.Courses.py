

course_count = {}
names = {}

while True:
    course = input()
    if course == "end":
        break
    courses = course.split(":")

    if courses[0] not in course_count:
        course_count[courses[0]] = 1
        names[courses[0]] = courses[1]
    else:
        course_count[courses[0]] += 1
        names[courses[0]] += courses[1]
for key, value in course_count.items():
    print(f"{key.strip()}: {value}")
    for i, v in names.items():
        if i == key:

            v_s = v.strip(" ").split(" ")

            for i1 in range(0, len(v_s), 2):
                value = v_s[i1] + " " + v_s[i1+1]
                print(f"-- {value}")

