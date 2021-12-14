class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

if __name__ == '__main__':
    my_dog = Dog('mango', 3)
    print('my_dog의 이름은 {}이고, 나이는 {}살입니다.'.format(my_dog.name, my_dog.age))