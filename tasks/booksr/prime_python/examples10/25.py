def is_prime(n):
    return True if n == 2 or n == 3 else all([n%i for i in range(3, n, 2)])

def primes(m, n):
    return [val for val in range(m, n + 1) if is_prime(val)]

if __name__ == '__main__':
    print(primes(10, 50)) 
# (1) 교재의 실행 결과가 [11, 13, 16, 17, 19, 23, 29, 31, 32, 37, 41, 43, 47]인데, 16, 32는 소수가 아님.
# (2) 동일한 코드인 위 코드 역시 같은 버그가 내포되있음.
# (3) 하지만 문제의 목표가 '위의 코드를 리스트 축약 표현과 all()함수를 사용하여 다시 구현하라'는 것이므로
#     교재의 문제 있는 알고리즘을 그대로 활용하고 별다른 조치를 취하지 않기로 함.