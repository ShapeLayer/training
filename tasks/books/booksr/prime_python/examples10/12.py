days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
li_1 = []
for day in days:
    li_1 += [day[:3].upper()]
li_2 = list(map(lambda day: day[:3].upper(), days))
li_3 = [day[:3].upper() for day in days]

if __name__ == '__main__':
    print(li_1)
    print(li_2)
    print(li_3)