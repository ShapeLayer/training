from typing import TypeVar, Generic
Numeric = TypeVar('Numeric', int, float)

class Rectangle(Generic[Numeric]):
    def __init__(self, x: Numeric, y: Numeric, w: Numeric, h: Numeric):
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h

    def __str__(self):
        return 'Rectangle : (x = {x}, y = {y}, w = {w}, h = {h}), 면적 : {a}'.format(x=self.get_x(), y=self.get_y(), w=self.get_width(), h=self.get_height(), a=self.area())

    def set_x(self, puts: Numeric) -> None:
        self.__x = puts
    def set_y(self, puts: Numeric) -> None:
        self.__y = puts
    def set_width(self, puts: Numeric) -> None:
        self.__width = puts
    def set_height(self, puts: Numeric) -> None:
        self.__height = puts
    
    def get_x(self) -> Numeric:
        return self.__x
    def get_y(self) -> Numeric:
        return self.__y
    def get_width(self) -> Numeric:
        return self.__width
    def get_height(self) -> Numeric:
        return self.__height
    
    def area(self) -> Numeric:
        return self.__width * self.__height

    def check_dot_in_range(self, x, y) -> bool:
        return (self.__x <= x and self.__x + self.__width >= x) and (self.__y >= y and self.__y - self.__height <= y)
    def overlaps(self, r: 'Rectangle') -> bool:
        return self.check_dot_in_range(r.__x, r.__y) or self.check_dot_in_range(r.__x + r.__width, r.__y - r.__height)
    def contains(self, r: 'Rectangle') -> bool:
        return self.check_dot_in_range(r.__x, r.__y) and self.check_dot_in_range(r.__x + r.__width, r.__y - r.__height)

if __name__ == '__main__':
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(0, -10, 10, 10)
    r3 = Rectangle(-100, 0, 120, 100)

    print('r1 = ', r1)
    print('r2 = ', r2)
    print('r3 = ', r3)
    
    print('r1 contains r2 :', r1.contains(r2))
    print('r1 contains r3 :', r1.contains(r3))
    print('r1 overlaps r2 :', r1.overlaps(r2))
    print('r1 overlaps r3 :', r1.overlaps(r3))