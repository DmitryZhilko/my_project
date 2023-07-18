class Employee:
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        return self.salary - self.salary * (20/100)
    
    def get_tax(self):
        return self.salary * (20/100)
    
person = Employee('Иванов Иван Иванович', 'Бухгалтер', 1000)
print(f'Имя работника: {person.name}\nДолжность: {person.position}\nЗарплата работника до удержания налогов: {person.salary} рублей')
print(f'Зарплата после удержания налогов: {person.get_salary()} рублей')
print(f'Сумма налога на зарплату: {person.get_tax()} рублей')

