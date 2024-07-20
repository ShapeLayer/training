text = input()
target = input()

'''
new = ''

for each in text:
    if each not in '0123456789':
        new += each

print(new)
'''

text_arr = list(text)
popped = 0
for i in range(len(text)):
    if text_arr[i - popped] in '0123456789':
        text_arr.pop(i - popped)
        popped += 1

text = ''.join(text_arr)
print(int(target in text))

