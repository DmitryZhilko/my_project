class Student():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grades):
        self.grades.append(grades)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
        
    
    def is_honors_student(self):
        if (sum(self.grades) / len(self.grades)) > 4.5:
            return True
        else:
            return False
        
my_student = Student('Иванов', 22)
my_student.add_grade(5)
my_student.add_grade(4)
my_student.add_grade(3)
print(f'Студент: {my_student.name}')
print(f'Оценки: {my_student.grades}')
print(f'Средни бал: {my_student.get_average_grade()}')
print(f'Средний бал больше 4.5: {my_student.is_honors_student()}')