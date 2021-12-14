new_list_1 = []
for i in range(1, 100):
    if i % 6 == 0:
        new_list_1 += [i]
new_list_2 = list(filter(lambda x: x if x % 6 == 0 else None, [i for i in range(1, 100)]))
new_list_3 = [i for i in range(6, 100, 6)]

if __name__ == '__main__':
    print('new_list =', new_list_1)
    print('new_list =', new_list_2)
    print('new_list =', new_list_3)