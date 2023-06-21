def compute(gets: str) -> str:
    if gets[:3] == '555':
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    print(compute(input()))
