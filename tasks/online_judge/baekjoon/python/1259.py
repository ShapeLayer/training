from math import floor
while True:
    puts = input()
    if puts == '0':
        break
    is_palindrome = True
    for i in range(floor(len(puts)/2)):
        if puts[i] == puts[-i-1]:
            continue
        else:
            is_palindrome = False
    print('yes' if is_palindrome else 'no')