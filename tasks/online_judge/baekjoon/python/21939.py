import heapq
from sys import stdin
input = stdin.readline

def compute(n: int, m: int, probs: list[tuple[int]], opers: list):
    easy_queue, hard_queue = [], []
    validate = {}
    output = []
    for prob, diff in probs:
        heapq.heappush(easy_queue, (diff, prob))
        heapq.heappush(hard_queue, (-diff, -prob))
        validate[prob] = diff
    for oper, args in opers:
        if oper == 'recommend':
            if args[0] == 1:
                diff, prob = heapq.heappop(hard_queue)
                while validate[-prob] != -diff:
                    diff, prob = heapq.heappop(hard_queue)
                output.append(-prob)
                heapq.heappush(hard_queue, (diff, prob))
            elif args[0] == -1:
                diff, prob = heapq.heappop(easy_queue)
                while validate[prob] != diff:
                    diff, prob = heapq.heappop(easy_queue)
                output.append(prob)
                heapq.heappush(easy_queue, (diff, prob))
        elif oper == 'add':
            prob, diff = args
            heapq.heappush(easy_queue, (diff, prob))
            heapq.heappush(hard_queue, (-diff, -prob))
            validate[prob] = diff
        elif oper == 'solved':
            validate[args[0]] = None
    return output

if __name__ == '__main__':
    n = int(input())
    probs = []
    for _i in range(n):
        probs.append(tuple(map(int, input().split())))
    m = int(input())
    opers = []
    for _i in range(m):
        gets = input().split()
        oper, args = gets[0], list(map(int, gets[1:]))
        opers.append([oper, args])
    print('\n'.join(map(str, compute(n, m, probs, opers))))
