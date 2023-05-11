MAX = int(1e10)
def compute(x: int, y: int):
    curr = (y * 100) // x
    
    def check(n):
        rate = ((y + n) * 100) // (x + n)
        return curr < rate
    
    low, high = 0, MAX
    while low + 1 < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid
    return low + 1

if __name__ == '__main__':
    x, y = map(int, input().split())
    if x == y:
        print(-1)
    else:
        result = compute(x, y)
        print(result if result != MAX else -1)
