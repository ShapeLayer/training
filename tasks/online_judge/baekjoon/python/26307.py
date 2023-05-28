def compute(hh: int, mm: int) -> int:
    return (hh - 9) * 60 + mm

if __name__ == '__main__':
    hh, mm = map(int, input().split())
    print(compute(hh, mm))
