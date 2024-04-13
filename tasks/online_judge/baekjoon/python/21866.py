gets = [*map(int, input().split())]
is_hacker = gets[0] > 100 or gets[1] > 100 or gets[2] > 200 or gets[3] > 200 or gets[4] > 300 or gets[5] > 300 or gets[6] > 400 or gets[7] > 400 or gets[8] > 500
if sum(gets) < 100:
    print('none')
elif is_hacker:
    print('hacker')
else:
    print('draw')
