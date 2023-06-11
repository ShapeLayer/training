from sys import stdin
input = stdin.readline

PI = 3.14159

def compute(gets: list[list[str]]) -> float:
    buf = []
    for get in gets:
        if get[0] == 'S':
            buf.append((4 / 3) * PI * (float(get[1]) ** 3))
        elif get[0] == 'C':
            buf.append((1 / 3) * PI * (float(get[1]) ** 3))
        else:
            buf.append(PI * (float(get[1]) ** 2) * float(get[2]))
    return max(buf)

if __name__ == '__main__':
    gets = []
    for _t in range(int(input())):
        gets.append(input().split())
    print(round(compute(gets), 3))
