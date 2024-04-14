cnt = 0
odd = 0
even = 0
while cnt < 10:
    n = int(input())
    if n % 2 == 1:
        odd += n
    else:
        even += n
    cnt += 1
print('odd = {}, even = {}'.format(odd, even))