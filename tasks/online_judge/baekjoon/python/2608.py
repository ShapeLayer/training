cvmap = {
    'rta': {'I': 1, 'a': 4, 'V': 5, 'b': 9, 'X': 10, 'c': 40, 'L': 50, 'd': 90, 'C': 100, 'e': 400, 'D': 500, 'f': 900, 'M': 1000},
    'atr': {1: 'I', 4: 'a', 5: 'V', 9: 'b', 10: 'X', 40: 'c', 50: 'L', 90: 'd', 100: 'C', 400: 'e', 500: 'D', 900: 'f', 1000: 'M'}
}

def roman_to_arabia(n: str) -> int:
    res = 0
    n = n.replace('IV', 'a')
    n = n.replace('IX', 'b')
    n = n.replace('XL', 'c')
    n = n.replace('XC', 'd')
    n = n.replace('CD', 'e')
    n = n.replace('CM', 'f')
    for s in n:
        res += cvmap['rta'][s]
    return res

def arabia_to_roman(n: int) -> str:
    res = ''
    while n > 0:
        if n >= 1000:
            res += 'M'
            n -= 1000
        elif n >= 900:
            res += 'CM'
            n -= 900
        elif n >= 500:
            res += 'D'
            n -= 500
        elif n >= 400:
            res += 'CD'
            n -= 400
        elif n >= 100:
            res += 'C'
            n -= 100
        elif n >= 90:
            res += 'XC'
            n -= 90
        elif n >= 50:
            res += 'L'
            n -= 50
        elif n >= 40:
            res += 'XL'
            n -= 40
        elif n >= 10:
            res += 'X'
            n -= 10
        elif n >= 9:
            res += 'IX'
            n -= 9
        elif n >= 5:
            res += 'V'
            n -= 5
        elif n >= 4:
            res += 'IV'
            n -= 4
        elif n >= 1:
            res += 'I'
            n -= 1
    return res

if __name__ == '__main__':
    a = roman_to_arabia(input())
    b = roman_to_arabia(input())
    c = a + b
    print(c)
    print(arabia_to_roman(c))
