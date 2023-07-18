class Car():
    
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, increase_speed):
        self.speed += increase_speed
        return self.speed
    
    def brake(self, slow_down):
        self.speed -= slow_down
        return self.speed
    
    def get_speed(self):
        print(f'Ваша текущая скорость:\n{self.speed} км/ч')
    
my_car = Car('Forf', 'Focus', '2018', 100)
print(f'Автомобиль: {my_car.make} {my_car.model}-{my_car.year}г.\nТекущая скорость: {my_car.speed} км/ч')
print('(Увеличим скорость на 10 км/ч)')
my_car.accelerate(10)
my_car.get_speed()
print('(Уменьшим скорость на 15 км/ч)')
my_car.brake(15)
my_car.get_speed()