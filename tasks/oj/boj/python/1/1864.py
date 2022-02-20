numeric = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1
}


# 첫번째 자리 숫자 처리
# 길이가 3이라고 했을 때 8**2 곱해져야함
# 길이가 4라고 했을 때 8**3 곱해져야함
# 두번째 자리 숫자 처리
# 길이가 3이라고 했을 때 8**1 곱해져야함
#                   len(puts) -1 -i (반복한 횟수, 0부터)

while True:
    puts = input()
    if puts == '#': break
    sums = 0
    for i in range(len(puts)):
        sums += numeric[puts[i]] * (8**(len(puts)-i-1))
    print(sums)