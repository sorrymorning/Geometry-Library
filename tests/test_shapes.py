import unittest
import math
from geometry_lib.shapes import Circle, Triangle, calculate_area

class TestShapes(unittest.TestCase):
    
    # --- Тесты для Круга (Circle) ---
    def test_circle_area(self):
        # Тест с радиусом 5
        circle = Circle(5)
        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected_area, places=7)

    def test_circle_area_zero_radius(self):
        # Тест на недопустимое значение (радиус <= 0)
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-10)

    # --- Тесты для Треугольника (Triangle) ---
    def test_triangle_area_heron(self):
        # Тест с известным результатом (стороны 3, 4, 5 - прямоугольный)
        triangle = Triangle(3, 4, 5)
        # Ожидаемая площадь: 0.5 * 3 * 4 = 6.0
        self.assertAlmostEqual(triangle.area(), 6.0, places=7)

    def test_triangle_area_equilateral(self):
        # Равносторонний треугольник со стороной 2
        triangle = Triangle(2, 2, 2)
        # Ожидаемая площадь: (sqrt(3)/4) * a^2 = (sqrt(3)/4) * 4 = sqrt(3)
        self.assertAlmostEqual(triangle.area(), math.sqrt(3), places=7)

    def test_triangle_invalid_sides(self):
        # Тест на несуществующий треугольник (неравенство треугольника)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10) # 1 + 2 <= 10
        # Тест на неположительные стороны
        with self.assertRaises(ValueError):
            Triangle(1, 2, -3)
            
    # --- Тесты для проверки на прямоугольный треугольник ---
    def test_triangle_is_right(self):
        # Прямоугольный: 5, 12, 13
        self.assertTrue(Triangle(5, 12, 13).is_right())
        # Прямоугольный: 3, 4, 5
        self.assertTrue(Triangle(3, 4, 5).is_right())
        # Непрямоугольный
        self.assertFalse(Triangle(3, 3, 3).is_right())
        # Непрямоугольный
        self.assertFalse(Triangle(5, 5, 5).is_right())
        # Непрямоугольный (небольшие отклонения)
        self.assertFalse(Triangle(5, 12, 13.001).is_right())
        
    # --- Тесты для полиморфизма (calculate_area) ---
    def test_calculate_area_polymorphism(self):
        circle = Circle(10)
        triangle = Triangle(6, 8, 10) # Площадь 24
        
        self.assertAlmostEqual(calculate_area(circle), math.pi * 100, places=7)
        self.assertAlmostEqual(calculate_area(triangle), 24.0, places=7)

if __name__ == '__main__':
    unittest.main()