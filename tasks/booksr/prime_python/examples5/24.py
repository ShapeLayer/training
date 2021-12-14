def get_divisor(puts: int) -> list:
    '''puts를 제외한 puts의 약수를 모두 반환합니다.'''
    return list(filter(None, [i if not puts % i else None for i in range(1, puts//2+1)]))

def writeln(puts: int, divs: list = None) -> None:
    '''puts가 완전수일 경우 지정된 형식에 맞춰 문장을 출력합니다.'''
    (print('{puts}은 완전수입니다\n{puts}의 약수: {divs}, 약수의 합 = {sum}'.format(puts=puts, divs=divs, sum=sum(divs))) if puts == sum(divs) else None) if divs else None

if __name__ == '__main__':
    [writeln(i, get_divisor(i)) for i in range(10001)]