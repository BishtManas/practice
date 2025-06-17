class Bank:

    def __init__ (self, amount=0):# Initial our bank balance is zero
        self.amount = amount
    
    def deb(self, amount2):# Amount2 for (debit amount).
        self.amount -= amount2
        print (f"{amount2} is debited.\nNow your account balance is {self.total_amount()}")
    
    def cre(self, amount3):# Amount3 for (credit amount).
        self.amount += amount3
        print (f"{amount3} is credited.\nNow your account balance is {self.total_amount()}")# We also call function from an another function like we done.
    
    def total_amount(self):# This function for checking total amount.
        if self.amount == 0 :
            print("Your account is empty!")# If account have no money then this statement works.
        else:
            print("Total balance in your account:-")
            return self.amount
        
info = Bank()# We create a object so that we can use it for all time.

while True:
    s = input("what do you want to do (credit=c, debit=d, see your balance=sb, exit=just enter) : ").lower().strip()# Ask to user what user wants to do.
    if s == "c":# use of if else statement for checking condition.
        n = int(input("what is your amount you want to credit : "))
        info.cre(n)
    elif s == "d":
        m = int(input("what is your amount you want to debit : "))
        info.deb(m)
    elif s == "sb":
        print(info.total_amount())
    elif s == "":
        print("Thank you !")
        break # Ater entering "enter" you are out of this loop.
    else:
        print("Invalid input! Please try again.")# If user print a different input then this condition works.
