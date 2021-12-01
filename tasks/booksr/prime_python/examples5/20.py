def process(src: str) -> str:
    '''
    문자열을 압축해서 반환합니다.
    '''
    if not src:
        return src
    content = ''
    cnt = 1
    for i in range(0, len(src)-1):
        if src[i] != src[i+1]:
            content += src[i] + str(cnt)
            cnt = 1
        else:
            cnt += 1
    content += src[-1] + str(cnt)
    return content

srcs = ('aaaabbb', 'aaaabccccaaaaacccfg', '', 'a')
# srcs = ('aaaabbb', 'aaaabccccaaaaacccfg', '', 'a', 'abcdefg', 'abcdefgg')
for src in srcs:
    print("src = '{}'\noutput = '{}'".format(src, process(src)))