MAX = int(1e7)
PRIME = [True for _i in range(MAX)]

def init():
    PRIME[0] = False
    PRIME[1] = False
    for i in range(3, MAX, 2):
        if PRIME[i]:
            for j in range(i + i, MAX, i):
                if not PRIME[j]: continue
                PRIME[j] = False

def compute(n: int) -> int:
    def check(n: int) -> bool:
        def is_pal(n: int) -> bool:
            buf: list[int] = []
            while n > 0:
                buf.append(n % 10)
                n //= 10
            for i in range(len(buf) // 2):
                if buf[i] != buf[-(i + 1)]:
                    return False
            return True
        def is_prime(n: int) -> bool:
            if n % 2 == 0:
                return n == 2
            return PRIME[n]
        return is_pal(n) and is_prime(n)

    while True:
        if check(n):
            return n
        else:
            n += 1

if __name__ == '__main__':
    init()
    n = int(input())
    print(compute(n))
