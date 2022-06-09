from math import ceil
gets = input()
limits = ceil(len(gets)/10)
for i in range(limits):
    if i - 1 == limits:
        print(gets[i*10:len(gets)])
    else:
        print(gets[i*10:(i+1)*10])
