def compute(get: str) -> str:
    return {
        'SONGDO': 'HIGHSCHOOL',
        'CODE': 'MASTER',
        '2023': '0611',
        'ALGORITHM': 'CONTEST'
    }[get]

if __name__ == '__main__':
    print(compute(input()))
