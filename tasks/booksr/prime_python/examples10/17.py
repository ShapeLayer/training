def partition(alist: list[int]) -> list[int]:
    new_list = alist
    idx = [1, len(alist)-1]
    while idx[0] < idx[1]:
        while new_list[idx[0]] < new_list[0]:
            idx[0] += 1
        while new_list[idx[1]] > new_list[0]:
            idx[1] -= 1
        new_list[idx[0]], new_list[idx[1]] = new_list[idx[1]], new_list[idx[0]]
    new_list[idx[0]], new_list[idx[1]] = new_list[idx[1]], new_list[idx[0]]
    new_list[0], new_list[idx[1]] = new_list[idx[1]], new_list[0]
    return new_list

if __name__ == '__main__':
    org_list = [8, 5, 12, 34, 3, 2, 97, 23, 45]
    print('org_list = ', org_list)
    print('partition(org_list)에 의해 정렬된 후의 리스트')
    print('new_list = ', partition(org_list))