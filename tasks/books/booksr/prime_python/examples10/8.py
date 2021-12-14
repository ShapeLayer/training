from functools import reduce
n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]

def my_max(li):
    m = li[0]
    for i in li:
        m = m if i < m else i
    return m

def my_min(li):
    m = li[0]
    for i in li:
        m = m if i > m else i
    return m

if __name__ == '__main__':
    # 1
    print('최댓값:', max(n_list))
    print('최솟값:', min(n_list))
    # 2
    print('최댓값:', my_max(n_list))
    print('최솟값:', my_min(n_list))
    # 3
    print('최댓값:', reduce(lambda a, b: a if a > b else b, n_list))
    print('최솟값:', reduce(lambda a, b: a if a < b else b, n_list))