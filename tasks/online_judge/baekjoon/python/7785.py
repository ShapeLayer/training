# WA
from sys import stdin
input = stdin.readline

enters = {}
for _i in range(int(input())):
    person, operation = input().split()
    if operation == 'enter':
        enters[person] = True
    else:
        if person in enters:
            enters[person] = False

for key in sorted(enters.keys()):
    if enters[key]:
        print(key)
