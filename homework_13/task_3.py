class BankAccount():
    
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def deposit(self, put_money):
        self.balance += put_money
        return self.balance
    
    def withdraw(self, withdraw_money):
        self.balance -= withdraw_money
        return self.balance

    def add_interest(self):
        if self.balance <= 0:
            return print('Баланс отрицательный или нулевой! Проценты не добавлены!')
        else:
            self.balance = self.balance + self.balance * (self.interest_rate / 100)
            return self.balance

my_bank_account = BankAccount(200, 5)
print(f'Сумма на счету: {my_bank_account.balance} р.;Процентная ставка: {my_bank_account.interest_rate}%')
print('(Положим на счет 20р.)')
my_bank_account.deposit(20)
print(f'Сумма на счету: \n{my_bank_account.balance} р.')
print('(Снимем со счета 10р.)')
my_bank_account.withdraw(10)
print(f'Сумма на счету: \n{my_bank_account.balance} р.')
print('(Добавим проценты на счет)')
my_bank_account.add_interest()
print(f'Сумма на счету: \n{my_bank_account.balance} р.')

  

