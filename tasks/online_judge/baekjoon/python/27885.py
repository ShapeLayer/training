from sys import stdin
input = stdin.readline
DAY = 86400

c, h = map(int, input().split())
timeline = []
for _i in range(c + h):
    h, m, s = map(int, input().split(':'))
    timeline.append(h * 60 * 60 + m * 60 + s)
timeline.sort()

prev = -40
total_passing = 0
for time in timeline:
    if time - prev >= 40:
        passing = 40
    else:
        passing = time - prev

    total_passing += passing
    prev = time

print(DAY - total_passing)
