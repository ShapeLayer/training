def compute(n: int, candies: list[int]) -> int:
    candies.sort(reverse=True)
    prev = None
    result = 0
    for candy in candies:
        if candy % 2 == 0:
            result += candy
        else:
            if prev:
                result += prev + candy
                prev = None
            else:
                prev = candy
    return result

if __name__ == '__main__':
    n = int(input())
    candies: list[int] = list(map(int, input().split()))
    print(compute(n, candies))
