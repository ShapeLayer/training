n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
new_list_2 = list(filter(lambda x: x % 12 == 0, n_list))
new_list_3 = [i for i in n_list if i % 12 == 0]

if __name__ == '__main__':
    print('n_list =', n_list)
    print('new_list =', new_list_2)
    print('new_list =', new_list_3)