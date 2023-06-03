def compute(weight: float, height: float) -> int:
    bmi = weight / (height * height)
    if bmi > 25:
        return 2
    elif 18.5 <= bmi <= 25:
        return 1
    else:
        return 0

if __name__ == '__main__':
    weight, height = float(input()), float(input())
    messages = ['Underweight', 'Normal weight', 'Overweight']
    res = compute(weight, height)
    print(messages[res])
