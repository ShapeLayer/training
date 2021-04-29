from sys import stdin
students, apple = [], []
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    students += [a]
    apple += [b]
s = 0
for i in range(len(students)):
    s += apple[i] - students[i]*(apple[i]//students[i])
print(s)