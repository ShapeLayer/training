from sys import stdin
input = stdin.readline

def fstr2hm(fstr: str) -> tuple[int]:
    return tuple(map(int, fstr.split(':')))

def compute(start: tuple[int], end: tuple[int], close: tuple[int], logs: tuple) -> int:
    participants = {}
    count = 0
    for log in logs:
        time, name = log
        if time <= start:
            participants[name] = 0
        elif end <= time <= close:
            if name in participants:
                if participants[name] == 0:
                    count += 1
                participants[name] += 1
    return count

if __name__ == '__main__':
    start, end, close = map(fstr2hm, input().split())
    log: list = []
    while True:
        try:
            gets = input().strip()
            if not gets: break
            time_fstr, name = gets.split()
            time = fstr2hm(time_fstr)
            log.append((time, name))
        except EOFError:
            break
    print(compute(start, end, close, log))
