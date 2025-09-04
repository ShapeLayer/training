N = int(input())
for i in range(N):
    print(f"String #{i + 1}")
    print("".join(chr((ord(each) - ord('A') + 1) % 26 + ord('A')) for each in input()))
    if i < N - 1: print()
