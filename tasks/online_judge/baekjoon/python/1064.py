def compute(coords: list[tuple[int]]) -> float:
    # (ax - bx)(ay - cy) = (ay - by)(ax - cx)
    if (coords[0][0] - coords[1][0]) * (coords[0][1] - coords[2][1]) == (coords[0][1] - coords[1][1]) * (coords[0][0] - coords[2][0]):
        return -1

    lines: list[float] = []
    for i in range(3):
        lines.append(((coords[i % 3][0] - coords[(i + 1) % 3][0]) ** 2 + (coords[i % 3][1] - coords[(i + 1) % 3][1]) ** 2) ** 0.5)

    lengths: list[float] = []
    for i in range(3):
        lengths.append((lines[i % 3] + lines[(i + 1) % 3]) * 2)

    return max(lengths) - min(lengths)
    
if __name__ == '__main__':
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    print(compute([(x1, y1), (x2, y2), (x3, y3)]))
