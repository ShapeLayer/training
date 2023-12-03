def compute(n: int, k: int, d: list[int]) -> list[int]:
    def _calc(score: int) -> int:
        p = (score * 100) // n
        if p <= 4: return 1
        elif p <= 11: return 2
        elif p <= 23: return 3
        elif p <= 40: return 4
        elif p <= 60: return 5
        elif p <= 77: return 6
        elif p <= 89: return 7
        elif p <= 96: return 8
        return 9
    return [*map(_calc, d)]

if __name__ == '__main__':
    n, k = map(int, input().split())
    d = [*map(int, input().split())]
    print(*compute(n, k, d))
