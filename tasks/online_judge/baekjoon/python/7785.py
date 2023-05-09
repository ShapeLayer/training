from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    people = {}
    for _i in range(int(input())):
        p, o = input().split()
        if p not in people:
            people[p] = 0
        if o == 'enter':
            people[p] += 1
        else:
            people[p] -= 1
    for name in sorted(people.keys(), reverse=True):
        if people[name] > 0:
            print(name)
