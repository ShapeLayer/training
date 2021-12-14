n_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
new_list_2 = list(filter(lambda x: x > 0, n_list))
new_list_3 = [i for i in n_list if i > 0]

if __name__ == '__main__':
    print('n_list =', n_list)
    print('new_list =', new_list_2)
    print('new_list =', new_list_3)