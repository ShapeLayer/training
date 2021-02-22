from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

hashtable = {}
for n in a:
    i = n % 10
    if i in hashtable:
        hashtable[i] += [n]
    else:
        hashtable[i] = [n]

print(b)
for i in b:
    is_exists = 0
    index = i % 10
    if index in hashtable:
        for j in hashtable[index]:
            print(j, 1)
            if j == m:
                is_exists = 1
    print(is_exists)