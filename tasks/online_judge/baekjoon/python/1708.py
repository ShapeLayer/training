from sys import stdin
input = stdin.readline

class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other) -> bool:
        return self.y < other.y or (self.y == other.y and self.x < other.x)
    
    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

def ccw(a: Dot, b: Dot, c: Dot) -> int:
    return a.x * b.y + b.x * c.y + c.x * a.y - b.x * a.y - c.x * b.y - a.x * c.y

def compute(n: int, dots: list[Dot]) -> int:
    dots.sort()

    hull_lower: list[Dot] = []
    # 볼록껍질의 아래 파트
    for dot in dots:
        while len(hull_lower) > 1:
            if ccw(hull_lower[-2], hull_lower[-1], dot) > 0:
                break
            hull_lower.pop()
        hull_lower.append(dot)

    # 볼록껍질의 위 파트
    hull_upper: list[Dot] = []
    for dot in dots[::-1]:
        while len(hull_upper) > 1:
            if ccw(hull_upper[-2], hull_upper[-1], dot) > 0:
                break
            hull_upper.pop()
        hull_upper.append(dot)

    return len(hull_lower) + len(hull_upper) - 2 # 양 끝점이 겹치므로 제외

if __name__ == '__main__':
    n = int(input())
    dots: list[Dot] = [Dot(*map(int, input().split())) for _i in range(n)]
    print(compute(n, dots))
