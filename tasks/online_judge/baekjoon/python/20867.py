def compute(m: float, s: float, g: float, a: float, b: float, l: float, r: float) -> str:
    l_time, r_time = l / a, r / b
    l_vel, r_vel = m / g + 1 if m % g else m / g, m / s + 1 if m % s else m / s

    if l_time + l_vel < r_time + r_vel:
        return 'friskus'
    else:
        return 'latmask'

if __name__ == '__main__':
    print(compute(*map(float, input().split()), *map(float, input().split()), *map(float, input().split())))
