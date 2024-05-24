from sys import stdin
from collections import Counter, defaultdict
input = stdin.readline

def compute(n: int, arr: list[int]):
    c = dict(Counter(arr))
    scores = defaultdict(list)
    score_achieved = defaultdict(list)
    score_sums = {}
    s = 1
    for i in range(n):
        now = arr[i]
        if c[now] < 6:
            continue
        scores[now].append(s)
        s += 1
    score_sums = { key: sum(scores[key][:4]) for key in scores }
    min_score = min(score_sums.values())
    min_scores = []
    for key in score_sums:
        if score_sums[key] == min_score:
            min_scores.append(key)
    if len(min_scores) > 1:
        min_5th_idx = list(scores.keys())[0]
        min_5th_val = scores[min_5th_idx][4]
        for key in scores:
            if min_5th_val > scores[key][4]:
                min_5th_val, min_5th_idx = scores[key][4], key
        return min_5th_idx
    return min_scores[0]

if __name__ == '__main__':
    for _t in range(int(input())):
        print(compute(int(input()), [*map(int, input().split())]))
