arr = [i + 1 for i in range(int(input()))]
while len(arr) > 1:
    new = []
    for i in range(len(arr)):
        now = arr.pop(0)
        if i % 2 == 1:
            new.append(now)
    arr = new
print(arr[0])
