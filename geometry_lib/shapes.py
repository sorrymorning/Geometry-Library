import math
from abc import ABC, abstractmethod
from typing import Union, List

# Абстрактный базовый класс для всех фигур
class Shape(ABC):
    """
    Абстрактный базовый класс для геометрических фигур.
    Требует реализации метода area().
    """
    @abstractmethod
    def area(self) -> Union[int, float]:
        """
        Вычисляет площадь фигуры.
        """
        pass

# Круг
class Circle(Shape):
    """
    Класс для представления круга.
    """
    def __init__(self, radius: Union[int, float]):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга
        """
        return math.pi * (self.radius ** 2)

# Треугольник
class Triangle(Shape):
    """
    Класс для представления треугольника по трем сторонам.
    """
    def __init__(self, side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]):
        sides = sorted([side_a, side_b, side_c])
        self.a, self.b, self.c = sides
        
        # Проверка на существование треугольника (неравенство треугольника)
        if self.a + self.b <= self.c:
            raise ValueError("Сумма двух сторон должна быть строго больше третьей стороны.")
        if any(s <= 0 for s in sides):
            raise ValueError("Все стороны должны быть положительными числами.")

    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона:
        A = sqrt(p * (p - a) * (p - b) * (p - c)), где p - полупериметр.
        """
        p = (self.a + self.b + self.c) / 2
        # Убедимся, что аргумент math.sqrt не отрицательный
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self, tolerance: float = 1e-9) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.
        Используется допуск (tolerance) для сравнения чисел с плавающей точкой.
        """
        # У нас стороны уже отсортированы: a <= b <= c. Гипотенуза - c.
        return abs(self.a**2 + self.b**2 - self.c**2) < tolerance

# ----------------------------------------------------------------------
# Дополнительная функция для "вычисления площади фигуры без знания типа фигуры"
# Это демонстрирует полиморфизм.
def calculate_area(shape: Shape) -> Union[int, float]:
    """
    Вычисляет площадь любой фигуры, которая наследуется от Shape и 
    реализует метод area().
    """
    return shape.area()