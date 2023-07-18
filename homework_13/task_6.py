class Dog():
    
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print('Гав-гав!')

    def get_human_age(self):
        return self.age * 7
    
my_dog = Dog('Рокки', 'Боксер', 5)
print(f'Кличка: {my_dog.name}\nПорода: {my_dog.breed}')
print(f'Возраст собаки в "человеческих" годах: {my_dog.get_human_age()}')