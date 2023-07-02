def compute(w1: int, h1: int, w2: int, h2: int) -> int:
    return 4 + 2 * max(w1, w2) + 2 * (h1 + h2)
    
if __name__ == '__main__':
    w1, h1, w2, h2 = int(input()), int(input()), int(input()), int(input())
    print(compute(w1, h1, w2, h2))
