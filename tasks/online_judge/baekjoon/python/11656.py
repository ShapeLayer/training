def compute(s: str) -> list[str]:
    result = [s[i:] for i in range(len(s))]
    return sorted(result)

if __name__ == '__main__':
    print('\n'.join(compute(input())))
