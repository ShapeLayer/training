def compute(text: str) -> str:
    length = len(text)
    ables = []
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                now = text[:j][::-1] + text[j:k][::-1] + text[k:][::-1]
                ables.append(now)
    return sorted(ables)[0]

if __name__ == '__main__':
    gets = input()
    print(compute(gets))
