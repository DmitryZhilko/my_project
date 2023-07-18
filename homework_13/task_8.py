class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Привет, меня завут {self.name} и мне {self.age} лет.')

    def can_vote(self):
        if self.age >= 18:
            return True
        else:
            return False

human = Person('Алексей', 15)
human.say_hello()
print(f'Возраст человека больше или равен 18 лет?\n{human.can_vote()}')