class Counter:
    def __init__(self, number: int = 0):
        self.__number = self.fix_range(number)
    
    def reset(self):
        self.__number = 0
    
    def fix_range(self, number):
        return number if not (number > 100 or number < 0) else 0
    
    def inc(self):
        self.__number += 1
        self.__number = self.fix_range(self.__number)

    def dec(self):
        self.__number -= 1
        self.__number = self.fix_range(self.__number)
    
    def __str__(self):
        return 'C({})'.format(self.__number)
    
    def __add__(self, other: 'Counter'):
        return self.fix_range(self.__number + other.__number)
    
    def __sub__(self, other: 'Counter'):
        return self.fix_range(self.__number - other.__number)

if __name__ == '__main__':
    c1 = Counter(10)
    c2 = Counter(20)
    c3 = c1 + c2
    c4 = c1 - c2
    print('c3 = ', c3)
    print('c4 = ', c4)