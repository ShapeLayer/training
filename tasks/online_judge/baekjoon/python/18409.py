def compute(n: int, name: str) -> int:
    count = 0
    for char in name:
        if char in 'aeiou':
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    name = input()
    print(compute(n, name))
