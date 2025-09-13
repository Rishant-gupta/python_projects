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
    
    def info(self):
        return f"Account owner: {self.owner}\tAccount balance: {self.__bankbalance}"
    
    def total():
        return f"{BankAccount.total_accounts}"
    
    def __del__(self):
        BankAccount.total_accounts -= 1
        return f"{self} is deleted"


    def deposit(self, ammount, pin=None):
        c=0
        if pin != self.__pin: 
            c+=1
            if c==3:
                return "Card blocked"
            return "Wrong pin"   
        else:
            self.__bankbalance += ammount
            return f"your bankbalance: {self.__bankbalance}"
            
    def withdraw(self, ammount1, pin=None):
        c=0
        if pin != self.__pin:
            c+=1
            if c==3:
                return "Card blocked"
            return "Wrong pin"
        else:
            if self.__bankbalance <=0 or ammount1 > self.__bankbalance :
             print("Insufficient balance")
            else:
              self.__bankbalance -= ammount1
            return f"your bankbalance: {self.__bankbalance}"
    def balance(self):
        return f"Your current balance: {self.__bankbalance}"
    
print("Press 1 to create account or press 2 to check details of existing account")
if int(input())==1:
    n = input("Enter your name: ")
    b = int(input("Enter your bank balance: "))
    p = int(input("Set your pin: "))

    acc1 = BankAccount(n, b, p)
    print("Account created successfully")
    print(f"Your acc information:{acc1.info()}")
else:
    print("wrong input")

c = int(input('''What task you want to perform?
      1.To Deposit press 1
      2.To Withdraw press 2
      3.To Check Balance press 3'''))


if c==1:
    ammount = int(input("Enter the ammount to be deposited: "))
    pin = int(input("Enter your pin: "))
    print(acc1.deposit(ammount, pin))
elif c==2:
    ammount1 = int(input("Enter the ammount to be withdrawn: "))
    pin = int(input("Enter your pin: "))
    print(acc1.withdraw(ammount1, pin))
elif c==3:
    print(acc1.info())
else:
    print("wrong input")


