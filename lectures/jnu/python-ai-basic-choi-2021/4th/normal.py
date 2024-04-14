# 교수 제시 방법 적용
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
for s in set(body):
    cnt[s] = 0
for s in body:
    cnt[s] += 1
for c in cnt:
    print(c, cnt[c])