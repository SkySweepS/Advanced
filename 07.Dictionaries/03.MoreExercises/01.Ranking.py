contest_dict1 = {}
while True:
    contest_password = input()
    if contest_password == "end of contests":
        break
    contest_split = contest_password.split(":")
    if contest_split[0] not in contest_dict1:
        contest_dict1[contest_split[0]] = contest_split[1]
sub_dict = {}
s_dict = {}
while True:
    sub_contest = input()
    if sub_contest == "end of submissions":
        break
    sub_split = sub_contest.split("=>")
    if sub_split[0] in contest_dict1: #Checking key
        if sub_split[1] in contest_dict1[sub_split[0]]: #Checking pass
            if sub_split[2] not in sub_dict:
                sub_dict[sub_split[2]] = int(sub_split[3])
                s_dict[sub_split[0]] = [sub_split[2], sub_split[3]]


            print(sub_dict[sub_split[2]])
            print(f"{sub_split[0]} - {sub_split[2]} - {sub_split[3]}")
print(sub_dict)
print(contest_dict1)