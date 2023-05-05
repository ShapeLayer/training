from sys import stdin
input = stdin.readline

def counts(content: str) -> list[int]:
    counts = [0, 0, 0, 0]
    for c in content:
        if c == 'L':
            counts[0] += 1
        elif c == 'O':
            counts[1] += 1
        elif c == 'V':
            counts[2] += 1
        elif c == 'E':
            counts[3] += 1
    return counts

def compute(yeondu: str, team: str) -> int:
    a, b = counts(yeondu), counts(team)
    L, O, V, E = a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

if __name__ == '__main__':
    yeondu = input()
    n = int(input())
    arr = [input().strip() for _i in range(n)]
    max_name, max_count = '', -1
    for name in arr:
        count = compute(yeondu, name)
        if count > max_count:
            max_name = name
            max_count = count
        elif count == max_count:
            if name < max_name:
                max_name = name
                max_count = count
    print(max_name)
