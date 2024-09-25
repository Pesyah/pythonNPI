"""
6. Написать класс Shape, который является родительским
для класса Square, который содержит конструктор, принимаю-
щий длину. Оба класса содержат метод area() для расчета пло-
щади. Причем класс Shape имеет площадь равную нулю
"""

# area сделал переменную, функцию для расчета немного изменил!
class Shape:
    area = 0
    side = 0

    def __init__(self, side):
        self.side = side
    
    def calculate_new_area(self, side):
        return self.area

class Square(Shape):
    
    def __init__(self, side):
        super().__init__(side) # делаю видимость, что наследование неообходимо
        self.area = side * side

    def calculate_new_area(self, side):
        self.area = side * side
        
new_shape = Square(10)
print(new_shape.area) # 100

new_shape1 = Square(15)
print(new_shape1.area) # 225
new_shape1.calculate_new_area(50)
print(new_shape1.area) # 2500