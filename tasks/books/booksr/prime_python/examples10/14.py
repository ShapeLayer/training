fruits = {'Apple': '사과', 'Strawberry': '딸기', 'Peach': '복숭아', 'Grape': '포도'}

li_1 = list(map(lambda key: '{} = {}'.format(key, fruits[key]), fruits))
li_2 = ['{} = {}'.format(key, fruits[key]) for key in fruits]

if __name__ == '__main__':
    print(li_1)
    print(li_2)