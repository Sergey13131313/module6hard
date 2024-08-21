import math


class Figure:
    """Базовый класс геометрических фигур"""
    SIDES_COUNT = 0

    def __init__(self, rgb, sides):
        if self.__is_valid_color(rgb):
            self.__rgb = rgb
        else:
            self.__rgb = [1 for x in range(3)]
        if self.__is_valid_sides(sides):
            self.__sides = sides
        else:
            self.__sides = [1 for i in range(self.SIDES_COUNT)]
        self.filled = False

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(self, rgb):
        flag = True
        if len(rgb) != 3:
            return False
        else:
            for x in rgb:
                if (isinstance(x, int) == False) or (x < 0 and x > 255):
                    flag = False
            return flag

    def get_color(self):
        return list(self.__rgb)

    def set_color(self, *rgb):
        if self.__is_valid_color(rgb):
            self.__rgb = rgb

    def __is_valid_sides(self, sides):
        return True if len(sides) == self.SIDES_COUNT else False

    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    """Класс фигуры круг"""
    SIDES_COUNT = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, sides)
        self.__sides = sides[0] / (2 * math.pi)

    def __len__(self):
        return int(2 * math.pi * self.__sides)

    def get_square(self):
        a = math.pi * math.sqrt(self.__sides)
        return a


class Triangle(Figure):
    """Класс фиругы треугольник"""
    SIDES_COUNT = 3

    def __init__(self, rgb, *sides):
        super().__init__(rgb, sides)

    def get_square(self):
        p = self.__len__()
        return math.sqrt(p * ((p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])))


class Cube(Figure):
    """Класс куб"""
    SIDES_COUNT = 12

    def __init__(self, rgb, *sides):
        super().__init__(rgb, sides)
        if self.__is_valid_sides(sides):
            self.__sides = [sides[0] for x in range(self.SIDES_COUNT)]
        else:
            self.sides = [1 for x in range(self.SIDES_COUNT)]

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_sides(self, sides):
        return True if len(sides) == 1 else False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = [new_sides[0] for i in range(self.SIDES_COUNT)]

    def get_volume(self):
        return math.pow(self.__sides[0], 3)


if __name__ == '__main__':
    circle = Circle((200, 200, 100), 10)
    triangle = Triangle((200, 200, 100), 10, 10, 15)
    cube1 = Cube((222, 35, 130), 6)

    print('Цвет круга - ', circle.get_color())
    print('Радиус круга - ', circle.get_sides())
    print('Длинна окружности - ', len(circle))
    print('Площадь круга - ', circle.get_square())
    circle.set_color(10, 10, 10)
    circle.set_sides(30, 30, 30)
    print('Цвет круга - ', circle.get_color())
    print('Радиус круга - ', circle.get_sides())
    print('Длинна окружности - ', len(circle))

    print('\n')

    print('Цвет треугольника - ', triangle.get_color())
    print('Стороны треугольника - ', triangle.get_sides())
    print('Периметр треугольника - ', len(triangle))
    print('Площадь треугольника - ', triangle.get_square())
    triangle.set_color(10, 10, 10)
    triangle.set_sides(30, 30, 30)
    print('Цвет треугольника - ', triangle.get_color())
    print('Стороны треугольника - ', triangle.get_sides())
    print('Периметр треугольника - ', len(triangle))

    print('\n')

    print('Печать цвет куба - ', cube1.get_color())
    print('Печать стороны куба - ', cube1.get_sides())
    print('Периметр куба - ', len(cube1))
    cube1.set_color(20, 20, 20)
    cube1.set_sides(10)
    print('Печать цвет куба - ', cube1.get_color())
    print('Печать стороны куба - ', cube1.get_sides())
    print('Периметр куба - ', len(cube1))
    print('Объем куба - ', cube1.get_volume())

    a = 10
