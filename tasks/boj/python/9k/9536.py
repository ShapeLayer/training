from sys import stdin

for _ in range(int(stdin.readline())):
    log = stdin.readline().rstrip().split()
    sounds, filtered = [], []
    while True:
        insert = stdin.readline().rstrip()
        if insert != 'what does the fox say?':
            a, __, b = insert.split()
            if a != 'fox':
                sounds += [b]
        else:
            break
    for sound in log:
        if sound not in sounds:
            filtered += [sound]
    print(' '.join(filtered))
