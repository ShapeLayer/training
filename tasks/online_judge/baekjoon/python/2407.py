from math import factorial as fact

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fact(n) // (fact(n - m) * fact(m)))
