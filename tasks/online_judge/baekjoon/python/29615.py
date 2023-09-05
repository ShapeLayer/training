def compute(n: int, m: int, pending: list, friends: list) -> int:
    return sum(int(each not in friends) for each in pending[:m])

if __name__ == '__main__':
    n, m = map(int, input().split())
    pending = input().split()
    friends = input().split()
    print(compute(n, m, pending, friends))
