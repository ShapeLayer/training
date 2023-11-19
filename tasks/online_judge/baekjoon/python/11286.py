import heapq

def compute(n: int, opers: list[int]) -> list[int]:
    output = []
    queue = []
    for oper in opers:
        if oper == 0:
            if not queue:
                output.append(0)
            else:
                output.append(heapq.heappop(queue)[1])
        else:
            heapq.heappush(queue, (abs(oper), oper))
    return output

if __name__ == '__main__':
    n = int(input())
    opers = [int(input()) for _i in range(n)]
    print('\n'.join(map(str, compute(n, opers))))
