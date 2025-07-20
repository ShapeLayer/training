import sys
input = sys.stdin.readline

def compute(N: int, scores: list) -> int:
    scores.sort()
    worst_s2 = scores[0][1]
    passed = 1

    for s1, s2 in scores:
        if worst_s2 > s2:
            passed += 1
            worst_s2 = s2
    
    return passed

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        scores = [tuple(map(int, input().split())) for _i in range(N)]
        print(compute(N, scores))
