from sys import stdin
input = stdin.readline

def compute(n: int, names: list[str]):
    def evaluate(a: str, b: str):
        length = min(len(a), len(b))
        result = False
        for i in range(1, length):
            if a[:i] == b[-i:]:
                result = True
                break
        return result
    result = 0
    for i in range(n):
        for j in range(i):
            if i == j: continue
            if evaluate(names[i], names[j]):
                result += 1
    return result

if __name__ == '__main__':
    n = int(input())
    names: list[str] = [input().strip() for _i in range(n)]
    print(compute(n, names))
