arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (len(arr) * 4)

def init(start: int, end: int, index: int):
    '''
    start(0, len(arr) - 1, 1)로 호출
    start: 배열의 시작 인덱스, end: 배열의 마지막 인덱스
    index: 트리의 인덱스
    트리 1번 인덱스 => 2번(좌측 절반), 3번(우측 절반)
        2번 인덱스 => 4번(좌측 절반), 5번(우측 절반)
            4번 인덱스 => 8번(좌측 절반), 9번(우측 절반)
            5번 인덱스 => 10번(좌측 절반), 11번(우측 절반)
        3번 인덱스 => 6번(좌측 절반), 7번(우측 절반)
            6번 인덱스 => 12번(좌측 절반), 13번(우측 절반)
            7번 인덱스 => 14번(좌측 절반), 15번(우측 절반)
    * 재귀 호출로 계속 아래 단계 트리에 접근
      상위 단계 트리는 하위 단계 트리 호출 결과를 활용하여 지정
      (하위 두 개의 트리 호출 결과의 합)
    * 범위를 계속 양분하므로, 인덱스는 2를 기준으로 처리됨
    '''
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid: int = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def get_sums(start: int, end: int, index: int, left: int, right: int):
    '''
    start, end: 호출 시 구해야 할 구간합 범위
    left, right: 최종적으로 구하고자 하는 구간합 범위
    index: 현재 참조할 트리 인덱스
    * 현재 구간이 최종 구간 안에 완전히 들어가 있을 때: 현재 index 참조 후 반환
    * 현재 구간이 최종 구간 안에 일부 들어가 있을 때: 구간을 양분하여 재귀 호출
    * 현재 구간이 최종 구간 바깥으로 완전히 나갔을 때: 0 반환
    '''
    if left > end or right < start:
        '''
        최종 구간의 시작점이 현재 구간 끝점보다 뒤에 나온다면 
        --<현재 구간>--| |--<최종 구간>--
        혹은 최종 구간의 끝점이 현재 구간의 시작점보다 먼저 나온다면
        --<최종 구간>--| |--<현재 구간>--
        0 반환 (구간 바깥)
        '''
        return 0
    if left <= start and right >= end:
        '''
        현재 구간이 최종 구간 안에 완전히 들어있을 때
        |==<최종 구간>==|--<현재 구간>--|==<최종 구간>==|
        '''
        return tree[index]
    '''
    위 두 경우가 전부 아닌 경우
    (= 현재 구간이 최종 구간에 걸쳐있을 때)
    '''
    mid: int = (start + end) // 2
    return get_sums(start, mid, index * 2, left, right) + get_sums(mid + 1, end, index * 2 + 1, left, right)

def update(start: int, end: int, index: int, target: int, delta):
    '''
    start, end: 구간 인덱스
    index: 현재 인덱스
    target: 수정 대상
    delta: 수정 대상의 변량
    수정 대상(target)은 구간 인덱스를 파악하여 범위 바깥으로 넘어갔는지 확인하기 위해 사용
    범위 안에 있으면 재귀 호출로 아래 단계 트리도 갱신
    '''
    if target < start or target > end:
        '''
        구간 바깥일 때 재귀 호출 중단
        '''
        return
    tree[index] += delta
    if start == end:
        '''
        마지막 단계까지 접근했다면 재귀 호출 중단
        '''
        return
    '''
    위 두 사례가 아니라면 재귀 호출
    '''
    mid: int = (start + end) // 2
    update(start, mid, index * 2, target, delta)
    update(mid + 1, end, index * 2 + 1, target, delta)

init(0, len(arr) - 1, 1) # 초기화

if __name__ == '__main__':
    # 0번부터 9번 인덱스까지 구간합 구하기
    # 트리 시작점이 1이므로 index는 1로 고정됨
    print(get_sums(start = 0, end = len(arr) - 1, index = 1, left = 0, right = 9))
    
    # 2번부터 6번 인덱스까지 구간합 구하기
    print(get_sums(start = 0, end = len(arr) - 1, index = 1, left = 0, right = 2))
    print()
    
    print('업데이트 전:')
    print(get_sums(0, len(arr) - 1, 1, 0, 4))
    # 배열 값 업데이트: arr[0]에 -1
    # 트리 시작점이 1이므로 index는 1로 고정됨
    update(start = 0, end = len(arr) - 1, index = 1, target = 0, delta = -1)
    print('업데이트 후:')
    # 0부터 4까지 구간합 구하기
    print(get_sums(0, len(arr) - 1, 1, 0, 4))
