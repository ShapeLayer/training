body = '''
Success is not the key to happiness.
Happiness is the key to success.
If you love what you are doing, you will be successful.
- Albert Schweitzer'''
body = body.replace(' ', '')
body = body.replace('\n', '')
body = body.replace('\t', '')
body = body.lower()
cnt = {}
for s in body:
    if s not in cnt:
        cnt[s] = 1
    else:
        cnt[s] += 1
for c in cnt:
    print(c, cnt[c])