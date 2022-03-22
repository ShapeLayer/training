from collections import Counter

gets = dict(Counter(input()))

counts = 1
center = ''
for key in gets:
    if gets[key] % 2 != 0:
        counts -= 1
        center = key
        if counts < 0:
            break

if counts < 0:
    print("I'm Sorry Hansoo")
else:
    body = ''
    for key in sorted(gets.keys()):
        body += key*(gets[key]//2)
    body = body + center + body[::-1]
    print(body)