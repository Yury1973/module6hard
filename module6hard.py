import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        self.__color = color
        if len(sides) == self.sides_count:
            self.__sides = sides
        elif len(sides) == 1:
            self.__sides = sides * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
        self.filled = filled


    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if (0 <= r < 256 and 0 <= g < 256 and 0 <= b < 256 and
                isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if isinstance(i, int) and i > 0:
                    return True
                else:
                    return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(*new_sides):
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__() / (2 * math.pi)

    def get_square(self):
        return self.__len__() ** 2 / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        return (self.__len__() / 2 * (self.__len__() / 2 - self.get_sides()[0]) *
                (self.__len__() / 2 - self.get_sides()[1]) * (self.__len__() / 2 - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма куба:
print(cube1.get_volume())
