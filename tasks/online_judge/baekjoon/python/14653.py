# WA
# https://www.acmicpc.net/board/view/115654

from sys import stdin
input = stdin.readline

n, k, q = map(int, input().split())
q -= 1
reads, senders = [], []

for _i in range(k):
    read_str, sender = input().strip().split()
    read = int(read_str)
    reads.append(read)
    senders.append(sender)

if reads[0] == 0:
    print(-1)
    exit()

represents = [False for _i in range(n)]
represents[0] = True
for i in range(k):
    if reads[q] <= reads[i]:
        represents[ord(senders[i]) - 65] = True

result = []
for i in range(n):
    if not represents[i]:
        result.append(chr(i + 65))

print(' '.join(result))
