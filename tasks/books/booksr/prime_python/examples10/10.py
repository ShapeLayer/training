new_list_1 = []
for i in range(1, 100):
    if i % 6 == 0 and i % 7 == 0:
        new_list_1 += [i]
new_list_2 = list(filter(lambda x: x if x % 6 == 0 and x % 7 == 0 else None, [i for i in range(1, 100)]))
new_list_3_a = [i for i in range(6*7, 100, 6*7)]
new_list_3_b = [i for i in range(1, 100) if i % 6 == 0 and i % 7 == 0]

if __name__ == '__main__':
    print('new_list =', new_list_1)
    print('new_list =', new_list_2)
    print('new_list =', new_list_3_a)
    print('new_list =', new_list_3_b)