def compute(t: str, p: str):
    n, m = len(t), len(p)

    def compute_fail_arr() -> list[int]:
        fail = [0 for _i in range(m)]
        
        prefix, i = 0, 1
        while i < m:
            '''
            `prefix`: 접두사 포인터
            `i`: 접미사 포인터
            '''
            if p[i] == p[prefix]:
                '''
                접두사(`prefix`)와 접미사(`i`)가 같다면 양 끝이 같은것임

                prefix += 1과 fail[i] = prefix는
                1. 다음 스텝에 처리할땐 접두사 포인터를 한칸 뒤로 밀어야 함
                2. fail[] 배열에 양 끝이 일치하는 부분의 길이를 넣으므로 `prefix`를 사용
                (1 차이를 이용하기 위해 `prefix += 1`을 먼저 처리)
                '''
                prefix += 1
                fail[i] = prefix
                i += 1
            else:
                '''
                접두사와 접미사가 같지 않다면
                
                 * 일반적일 때 (prefix != 0)
                    `prefix`가 가리키는 접두사 경계를 한 차례 앞으로 당김
                 * 접두사 경계가 가장 앞에 있을 때 (prefix == 0)
                    더 이상 접두사를 앞으로 당길 수 없는데도 접미사와 같은 부분이 없으므로
                    양 끝에 같은 부분이 없다고 생각할 수 있음
                '''
                if prefix != 0:
                    prefix = fail[prefix - 1]
                else:
                    fail[i] = 0
                    i += 1
        return fail
    
    def kmp(fail: list[int]):
        '''
        `i`: 텍스트(`t`)의 접두사 오른쪽 끝부분 인덱스를 저장
        `j`: 패턴(`p`)의 접두사 오른쪽 끝부분 인덱스를 저장
        `founds`: 매치되는 문자열의 시작 인덱스
        '''
        i, j = 0, 0
        founds: list[int] = []
        while i < n:
            if t[i] == p[j]:
                '''
                텍스트와 패턴의 접두사 끝부분 인덱스가 같다면, 접두사 길이를 한 칸 늘림
                '''
                i += 1
                j += 1
            if j == m:
                '''
                패턴 접두사 끝부분 인덱스가 패턴 길이만큼 늘어난 경우
                (= 패턴 전부를 검사한 경우)

                매치된 것이므로 매치 처리
                패턴의 접두사 포인터는 패턴을 찾지 못한것처럼 이동 처리
                '''
                founds.append(i - m + 1)
                j = fail[j - 1]
            elif i < n and t[i] != p[j]:
                '''
                아직 패턴 매치가 덜 끝났고 (i가 여전히 n보다 작고, while의 루프 조건)
                패턴 접두사 끝부분이 `t`, `p` 서로 다른 경우

                1. 패턴의 접두사 포인터가 제일 앞에 있지 않다면 실패함수(`fail[x]`) 값에 따라 적절하게 인덱스 조정
                2. 제일 앞에 있다면 다음 패턴으로 매치
                '''
                if j != 0:
                    j = fail[j - 1]
                else:
                    i += 1
        return founds

    fail = compute_fail_arr()
    founds = kmp(fail)
    return founds

if __name__ == '__main__':
    t, p = input(), input()
    founds = compute(t, p)
    print(len(founds))
    for each in founds:
        print(each)
