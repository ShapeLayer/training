TABLE = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy'
}

def compute(name: str) -> str:
    return TABLE[name]

if __name__ == '__main__':
    print(compute(input()))
