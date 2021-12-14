# (1)
def flatten(list_2d: list) -> list:
    content = []
    for list_ in list_2d:
        for item in list_:
            content += [item]
    return content

# (2)
def flatten_(list_2d: list) -> list:
    return [item for list_ in list_2d for item in list_]

if __name__ == '__main__':
    sample = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print('org_list = ', sample)
    print('new_list = ', flatten(sample))
    print('org_list = ', sample)
    print('new_list = ', flatten_(sample))