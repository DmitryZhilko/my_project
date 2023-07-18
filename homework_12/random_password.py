import random

file = open('slova.txt', 'r')                                 
file_read = file.read()                                      
split_file_read = file_read.split(',')                          
two_words = random.sample(split_file_read, 2) 
first_word = two_words[0]  
second_word = two_words[1] 
password = first_word.title() + second_word.title()             

class MyLenError(Exception):
    def __init__(self, first_word):
        self.first_word = first_word
       
        
        
try:
    if len(first_word) < 3 or len(second_word) < 3:
        raise Exception(f'{password}-{len(password)} букв\nОшибка, одно из слов меньше 3 букв')
    if len(password) < 8  or len(password) > 10:
        raise MyLenError(f'{password}-{len(password)} букв\nОшибка, пароль не верной длины!')
except Exception as mr:
    print(mr)
except MyLenError as mvr:
    print(mvr)
else:
    print(f'Ваш пороль:\n{password}-{len(password)} букв')
finally:
    file.close()
