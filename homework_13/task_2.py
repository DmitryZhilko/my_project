class Rectangle():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * (self.width + self.height)
        
a = Rectangle(5, 6)
print(f'Ширина: {a.width}; Высота: {a.height}')
print(f'Площадь прямоугольника: {a.get_area()}')
print(f'Периметр прямоугольника: {a.get_perimeter()}')