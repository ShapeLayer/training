from sys import stdin
input = stdin.readline

def compute(n: int, numbers: list[str]):
    numbers.sort()
    ends = {}
    def query(number: str) -> bool:
        ln = len(number)
        for i in range(1, ln + 1):
            key = number[:i]
            if key in ends and ends[key]:
                return False
        ends[number] = True
        return True
    for number in numbers:
        if not query(number):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _i in range(t):
        n = int(input())
        numbers = [input().strip() for _i in range(n)]
        print('YES' if compute(n, numbers) else 'NO')
