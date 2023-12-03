SCORES = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]

def compute(gets: str) -> bool:
    converts = [SCORES[ord(each) - 65] for each in gets]
    while len(converts) > 1:
        new = [(converts[2 * i] + converts[2 * i + 1]) % 2 for i in range(len(converts) // 2)]
        if len(converts) % 2 == 1:
            new.append(converts[-1])
        converts = new
    return converts[0] % 2 == 1
    
if __name__ == '__main__':
    print("I'm a winner!" if compute(input()) else "You're the winner?")
