import random
arr = [0 for i in range(6)]
# arr = [0, 0, 0, 0, 0, 0] 이랑 똑같음
for i in range(1200):
    value = random.randint(0, 5)
    arr[value] += 1
for i in range(6):
    print('주사위 %d 나온 횟수 : %d' % (i+1, arr[i]))