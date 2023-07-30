class Soda():
    def __init__(self, addition):
        if isinstance(addition, str):
            self.addition = addition
        else:
            self.addition = None
    
    def show_my_drink(self):
        if self.addition:
            print(f'Газировка и {self.addition}')
        else:
            print('Обычная газировка')
    
drink = Soda(5)
drink.show_my_drink()
drink_2 = Soda('cherry')
drink_2.show_my_drink()