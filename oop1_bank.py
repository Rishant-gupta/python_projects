'''
Bank ATM Simulation  
Problem Statement:
The program should allow a user to interact with an ATM machine, perform basic banking 
operations, and ensure data security.  
Requirements  
• Create a class ATM with private attributes: balance, pin.  
• Implement methods: check_balance(pin), deposit(amount, pin), withdraw(amount, 
pin).  
• Handle wrong PIN attempts and insufficient balance.  
• Optional: Support multiple users, SavingsAccount and CurrentAccount subclasses. 
'''

class BankAccount():
    total_accounts = 0
    def __init__(self, owner, bankbankbalance=0, pin=1234):
        self.owner= owner
        self.__bankbalance= bankbankbalance
        self.__pin= pin

        BankAccount.total_accounts += 1
        with open(f"{self.owner}_passbook.txt", "a") as f:
            f.write(f"Account created for {self.owner} with initial balance {self.__bankbalance}\n")
    
    def info(self):
        return f"Account owner: {self.owner}\tAccount balance: {self.__bankbalance}"
    
    def total():
        return f"{BankAccount.total_accounts}"
    
    def __del__(self):
        BankAccount.total_accounts -= 1
        return f"{self} is deleted"
    
    def passbook(self):
        with open(f"{self.owner}_passbook.txt", "r") as f:
            content = f.read()
        return content

    def deposit(self, ammount, pin=None):
        attempt = 1
        F = True
        while F == True:
            if pin == self.__pin: 
                self.__bankbalance += ammount
                with open(f"{self.owner}_passbook.txt", "a") as f:
                    f.write(f"Deposited {ammount}. New balance: {self.__bankbalance}\n")
                F = False
                return f"your bankbalance: {self.__bankbalance}"
            else:
                print("Entered pin is wrong: ")
                pin = int(input("Enter the pin again: "))
                attempt += 1
                if attempt == 3:
                    F = False
                    return f"you enetred wrong pin 3 times, your card is blocked"
                    
    
            
    def withdraw(self, ammount1, pin=None):
        B = True
        while B == True:
            if pin == self.__pin:
                self.__bankbalance -= ammount1
                with open(f"{self.owner}_passbook.txt", "a") as f:
                    f.write(f"Withdrew {ammount1}. New balance: {self.__bankbalance}\n")
                B = False
                return f"your bankbalance: {self.__bankbalance}"
            else:
                print("Entered pin is wrong: ") 
                pin = int(input("Enter the pin again: "))
           
    def balance(self):
        return f"Your current balance: {self.__bankbalance}"
    
print("create account: ")
A = False
n = input("Enter your name: ")
b = int(input("Enter your bank balance: "))
while True:
    p = int(input("Set your 4 digit pin: "))
    if 999< p <10000:                                             
        acc1 = BankAccount(n, b, p)
        print("Account created successfully")
        print(f"Your acc information:{acc1.info()}")
        A = True
        break
    else:
        print("Pin should be 4 digit")

if A == True:
    c = int(input('''What task you want to perform?
         1.To Deposit press 1
         2.To Withdraw press 2
         3.To Check Balance press 3
         4.To View Passbook press 4: '''))

    if c==1:
        ammount = int(input("Enter the ammount to be deposited: "))
        pin = int(input("Enter your pin: "))
        print(acc1.deposit(ammount, pin))
    if c==2:
        ammount1 = int(input("Enter the ammount to be withdrawn: "))
        pin = int(input("Enter your pin: "))
        print(acc1.withdraw(ammount1, pin))
    elif c==3:
        print(acc1.info())
    elif c==4:
        print(acc1.passbook())
else:
    print("wrong input")


