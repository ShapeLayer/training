REVERSE: dict = {
    'I': 'E', 'E': 'I',
    'N': 'S', 'S': 'N',
    'T': 'F', 'F': 'T',
    'P': 'J', 'J': 'P'
}

def compute(mbti: str) -> str:
    buf = []
    for c in mbti:
        buf.append(REVERSE[c])
    return ''.join(buf)

if __name__ == '__main__':
    mbti = input()
    print(compute(mbti))
