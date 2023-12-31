from sys import stdin
input = stdin.readline

s = [
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]
for _i in range(int(input())):
    if input().strip() not in s:
        print('Yes')
        exit()
print('No')
