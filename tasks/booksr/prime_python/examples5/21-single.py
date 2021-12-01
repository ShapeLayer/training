def process(src: str) -> str:
    '''
    압축한 문자열을 해제하여 반환합니다.
    단, 압축한 문자열의 정수부(숫자부분)은 9를 넘을 수 없습니다.
    '''
    return ''.join([src[i-1]*int(src[i]) for i in range(1, len(src), 2)])

if __name__ == '__main__':
    [print("src = '{}'\noutput = '{}'".format(src, process(src))) for src in ('a2b3c6a2c3f1g1', )]
    # [print("src = '{}'\noutput = '{}'".format(src, process(src))) for src in ('a2b3c6a2c3f1g1', 'a2b3c3')] # Debug