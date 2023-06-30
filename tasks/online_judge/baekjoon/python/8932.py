def calc_track_type(a: int, b: int, c: int, p: int) -> int:
    return int(a * (b - p) ** c)

def calc_field_type(a: int, b: int, c: int, p: int) -> int:
    return int(a * (p - b) ** c)

def compute(hurdle: int, jump_up: int, throw_shot: int, run_200: int, jump_forward: int, throw_spear: int, run_800: int) -> float:
    return calc_track_type(9.23076, 26.7, 1.835, hurdle) + \
        calc_field_type(1.84523, 75, 1.348, jump_up) + \
        calc_field_type(56.0211, 1.5, 1.05, throw_shot) + \
        calc_track_type(4.99087, 42.5, 1.81, run_200) + \
        calc_field_type(0.188807, 210, 1.41, jump_forward) + \
        calc_field_type(15.9803, 3.8, 1.04, throw_spear) + \
        calc_track_type(0.11193, 254, 1.88, run_800)

if __name__ == '__main__':
    for _t in range(int(input())):
        print(compute(*map(int, input().split())))
