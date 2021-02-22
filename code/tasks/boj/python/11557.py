from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    schools = {}
    for __ in range(n):
        school, alcohol = stdin.readline().split()
        alcohol = int(alcohol)
        schools[alcohol] = school
    print(schools[max(schools.keys())])