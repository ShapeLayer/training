def compute(char: str) -> str:
    repeats, _ord = 0, ord(char)
    while _ord:
        repeats += _ord % 10
        _ord //= 10
    return char * repeats

if __name__ == '__main__':
    for each in map(compute, input()):
        print(each)
