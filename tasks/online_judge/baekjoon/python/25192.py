from collections import defaultdict

def compute(n: int, gets: list[str]) -> int:
    senders: defaultdict = defaultdict(int)
    sends: int = 0
    for each in gets:
        if each == 'ENTER':
            senders = defaultdict(int)
        else:
            if senders[each] == 0:
                sends += 1
                senders[each] += 1
    return sends

if __name__ == '__main__':
    n = int(input())
    gets: list[str] = [input().strip() for _i in range(n)]
    print(compute(n, gets))
