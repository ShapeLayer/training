def compute(gets: str) -> int:
    result = len(gets)
    for char in gets:
        if char == ':':
            result += 1
        elif char == '_':
            result += 5
    return result

if __name__ == '__main__':
    print(compute(input()))
