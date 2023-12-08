vowels = 'aeiouAEIOU'

if __name__ == '__main__':
    for _i in range(int(input())):
        s = input()
        c, v = 0, 0
        for each in s:
            if each in vowels:
                v += 1
            elif each.isalpha():
                c += 1
        print(c, v)
