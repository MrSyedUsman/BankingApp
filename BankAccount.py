class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_details(self):
        print(  "User Information \n"  )
        print("NAME : {}".format(self.name))
        print("AGE : {}".format(self.age))
        print("GENDER : {}\n".format(self.gender))

class BankAccount(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, cash):
        self.cash = cash
        self.balance = self.balance + self.cash
        print("Deposited {0} RS\n Updated Balance : {1} RS\n".format(self.cash,self.balance))

    def cashout(self, cash):
        self.cash = cash
        if (self.cash > self.balance):
            print("Insufficient Funds!")
            print("Balance :", self.balance)
        else:
            self.balance = self.balance - cash
            print("Withdrawn {0} RS\n Updated Balance : {1} RS\n".format(self.cash,self.balance))

    def show_balance(self):
        self.print_details()
        print("Balance : {}\n".format(self.balance))

    

usman = BankAccount("Usman", 20, "Male")
usman.show_balance()
usman.deposit(1000)
usman.cashout(450)
usman.show_balance()








