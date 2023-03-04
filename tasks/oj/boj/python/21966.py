n = int(input())
puts = input()
if n <= 25: print(puts)
elif '.' not in puts[12:-12]:
    print('{}...{}'.format(puts[:11], puts[-11:]))
else:
    print('{}......{}'.format(puts[:9], puts[-10:]))