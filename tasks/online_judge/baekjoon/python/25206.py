total_score, total_unit = 0.0, 0.0
a2n = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}
for _i in range(20):
    name, unit, score = input().split()
    if score == 'P': continue
    unit = float(unit)
    total_score += a2n[score] * unit
    total_unit += unit
print(total_score / total_unit)
