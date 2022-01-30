for _ in range(int(input())):
    counts = {chr(i): 0 for i in range(97, 123)}
    puts = input().strip().lower()
    for word in puts:
        if 97 <= ord(word) <= 122:
            counts[word] += 1
    s = set(counts.values())
    if 0 in s:
        print('Case {}: Not a pangram'.format(_+1))
    elif 1 in s:
        print('Case {}: Pangram!'.format(_+1))
    elif 2 in s:
        print('Case {}: Double pangram!!'.format(_+1))
    else:
        print('Case {}: Triple pangram!!!'.format(_+1))