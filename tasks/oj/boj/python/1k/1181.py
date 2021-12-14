from sys import stdin

words = {}

for _ in range(int(stdin.readline())):
    w = stdin.readline().rstrip()
    n = len(w)
    if n in words:
        if w not in words[n]:
            words[n] += [w]
    else:
        words[n] = [w]

for l in sorted(words.keys()):
    for word in sorted(words[l]):
        print(word)
