gets = [[], []]
for i in range(2):
    for j in range(10):
        gets[i] += [int(input())]
    gets[i].sort()
scores = [0, 0]
for i in range(2):
    for j in range(3):
        scores[i] += gets[i].pop()
print(scores[0], scores[1])
