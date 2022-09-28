from sys import stdin
input = stdin.readline

arr = []
tree = []

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)
    return tree[index]

def get_value(start, end, index, left, right):
    if left > end or right < start: return 1
    if left <= start and right >= end: return tree[index]
    mid = (start + end) // 2
    return get_value(start, mid, index * 2, left, right) * get_value(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, target, value):
    # update 함수의 역전파 방식 잘 알아놓기
    # WA의 원인: 기존에는 tree 업데이트를 수행한 다음 return (null)만 함
    if target < start or target > end: return tree[index]
    # Value is 1, 0, or -1
    tree[index] = value
    if start == end: return tree[index]
    mid = (start + end) // 2
    lt = update(start, mid, index * 2, target, value)
    rt = update(mid + 1, end, index * 2 + 1, target, value)
    tree[index] = lt * rt
    return tree[index]

if __name__ == '__main__':
    while True:
        try: n, k = map(int, input().split())
        except (ValueError, EOFError): break
        arr = [1 if i > 0 else (-1 if i < 0 else 0) for i in map(int, input().split())]
        tree = [0 for _ in range(n*4)]
        init(0, n-1, 1)
        string = ''
        for _i in range(k):
            cmd = input().split()
            if cmd[0] == 'C':
                i, v = int(cmd[1]), int(cmd[2])
                v = 1 if v > 0 else (-1 if v < 0 else 0)
                if arr[i-1] == 0:
                    arr[i-1] = v
                    init(0, n-1, 1)
                elif arr[i-1] != v:
                    arr[i-1] = v
                    update(1, n, 1, i, v)
            elif cmd[0] == 'P':
                i, j = int(cmd[1]), int(cmd[2])
                res = get_value(1, n, 1, i, j)
                if res > 0: string += '+'
                elif res < 0: string += '-'
                else: string += '0'
        print(string)