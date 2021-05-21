from sys import stdin

users = {}
for _ in range(int(stdin.readline())):
    age, name = stdin.readline().rstrip().split()
    # 사전순: 10 11 3 9 ...
    # 숫자순: 3 9 10 11 ...
    age = int(age)
    if age in users:
        users[age] += [name]
    else:
        users[age] = [name]

for age in sorted(users.keys()):
    for name in users[age]:
        print(age, name)
