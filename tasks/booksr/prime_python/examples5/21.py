def process(src: str) -> str:
    '''
    압축한 문자열을 해제하여 반환합니다.
    '''
    content = ''
    cnt = '0'
    ready = ''
    for i in range(len(src)):
        if ord(src[i]) in range(48, 58):
            cnt += src[i]
        if ord(src[i]) not in range(48, 58) or i == len(src)-1:
            content += ready * int(cnt)
            if i != len(src)-1:
                ready = src[i]
                cnt = '0'
    return content

if __name__ == '__main__':
    for src in ('a2b3c6a2c3f1g1', ):
        print("src = '{}'".format(src))
        print("output = '{}'".format(process(src)))
    # [print(process(src)) for src in ('a2b3c6a2c3f1g1', 'a1', '', 'a10', 'a100')] # Debug