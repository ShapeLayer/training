from sys import argv


socks = open('socks').read()
if len(argv) > 1:
    for line in socks.split('\n'):
        for n in range(len(line)):
            if n > int(argv[1]):
                print(line[n], end='')
        print()
else:
    print(socks)