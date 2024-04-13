from sys import stdin
input = stdin.readline

for _i in range(int(input())):
    cm, kg = map(int, input().split())
    bmi = kg / ((cm * .01) ** 2)
    if cm < 140.1:
        print(6)
    elif cm < 146:
        print(5)
    elif cm < 159:
        print(4)
    elif cm < 161:
        if 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    elif cm < 204:
        if 20 <= bmi < 25:
            print(1)
        elif 18.5 <= bmi < 30:
            print(2)
        elif 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    else:
        print(4)
