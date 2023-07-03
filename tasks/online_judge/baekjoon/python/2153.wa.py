def compute(gets: str) -> bool:
    n: int = 0
    for char in gets:
        if 97 <= ord(char):
            n += ord(char) - 96
        else:
            n += ord(char) - 65 + 27

    is_prime: list[bool] = [True for _i in range(n + 1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return is_prime[n]

if __name__ == '__main__':
    print('It is a prime word.' if compute(input()) else 'It is not a prime word.')
