class BankAccount:
    def __init__(self, acnt):
        self.acnt = acnt
        self.balance = 0

    def deposit(self, amt):
        print(f'통장에 {amt}원이 입급됨.')
        self.balance += amt
        print(f'현재 잔액은 {self.balance}')        
        return self.balance

    def withdraw(self, amt):
        print(f'통장에 {amt}원이 출금됨.')
        self.balance -= amt
        print(f'현재 잔액은 {self.balance}\n')   

a = BankAccount('123~456')
a.deposit(10000)
a.withdraw(5000)

b = BankAccount('456~789')
b.deposit(2000)
