def compute(gets: str) -> int:
    dp = {}
    ln = len(gets)
    for i in range(ln):
        for j in range(i + 1, ln + 1):
            key = gets[i:j]
            if key not in dp:
                dp[key] = True
    return len(dp)

if __name__ == '__main__':
    print(compute(input()))
