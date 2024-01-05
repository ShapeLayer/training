gets = ''
while True:
    try:
        gets = input()
    except EOFError:
        break
    lower, upper, number, whitespace = 0, 0, 0, 0
    for s in gets:
        if 97 <= ord(s) <= 122:
            lower += 1
        elif 65 <= ord(s) <= 90:
            upper += 1
        elif 48 <= ord(s) <= 57:
            number += 1
        elif s == ' ':
            whitespace += 1
    print(lower, upper, number, whitespace)
