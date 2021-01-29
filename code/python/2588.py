num1 = int(input())
num2 = str(input())

for i in range(3):
    print(num1 * int(num2[2-i]))

print(num1 * int(num2))