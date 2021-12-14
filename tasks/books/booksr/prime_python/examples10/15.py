fruits = {'Apple': '사과', 'Strawberry': '딸기', 'Peach': '복숭아', 'Grape': '포도'}
encode = list(map(lambda key: '{} = {}'.format(key, fruits[key]), fruits))
# Method 1 (example)

# Method 2
decode_1 = {}
for item in encode:
    key, value = item.split(' = ')
    decode_1[key] = value
decode_2 = dict((key, value) for key, value in [item.split(' = ') for item in encode])

if __name__ == '__main__':
    print('fruits_list =', encode)
    print('fruits =', decode_1)
    print('fruits =', decode_2)