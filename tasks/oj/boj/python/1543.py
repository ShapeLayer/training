doc = input()
key = input()
cnt = 0
i = 0

while i < len(doc):
    if doc[i:i+len(key)] == key:
        cnt += 1
        i += len(key)
    else:
        i += 1

print(cnt)