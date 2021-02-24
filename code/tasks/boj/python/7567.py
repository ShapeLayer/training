plates = input()
height = 0
for p in range(len(plates)):
    if p == 0:
        height += 10
    else:
        if plates[p-1] == plates[p]:
            height += 5
        else:
            height += 10
print(height)