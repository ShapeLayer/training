from sys import stdin
input = stdin.readline

def compute(code: str, gets: str) -> bool:
    res = []
    for i in range(len(gets)):
        if code[i] != '*' and code[i] != gets[i]:
            return False
    return True

if __name__ == '__main__':
    code: str = input().strip()
    n: int = int(input())
    result: list[str] = []
    for _t in range(n):
        gets: str = input().strip()
        if compute(code, gets):
            result.append(gets)
    print(len(result))
    for each in result:
        print(each)
