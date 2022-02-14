case = 0
puts = list(map(int, input().split()))
for i in range(8):
    if i == 0 and puts[i] == 8:
        case = 1
    if case == 0:
        if i + 1 != puts[i]:
            case = 2
    elif case == 1:
        if 8 - i != puts[i]:
            case = 2
if case == 0:
    print('ascending')
elif case == 1:
    print('descending')
else:
    print('mixed')