class budget:
    def __init__(self,item,brand,amount):
        self.item=item
        self.brand=brand
        self.amount=amount

    def deposit(self):
        print(f'make deposit in {self.item}')
    @classmethod
    def how_much(cls):
        int(input(f'How much would you like to deposit \n'))
        

    def check_balance(self):
        print(f'check balance of {self.item}')
        print('current balance')
    def transfer(self):
        print(f'Make transfer to {self.item}')
    @classmethod
    def transfer_money(cls):
        int(input('How much would you like to transfer \n'))
        
    def withdraw(self):
        print(f'Make withdrawal from {self.item}')
    @classmethod
    def withdrawal(cls):
        int(input('How much would you like to withdrawal \n'))
