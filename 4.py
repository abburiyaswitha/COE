class Bank:
    accbal = 10000  
    def viewOptions(self):
        print("1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Exit")
    def deposit(self):
        amount = int(input("Enter an amount to deposit:"))
        if 100 < amount and amount % 100 == 0 and amount < 50000:
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount.")
    def withdraw(self):
        attempts = 0  
        while attempts < 3:
            amount = int(input("Enter an amount to withdraw:"))
            if 100 < amount and amount % 100 == 0 and amount < self.accbal and self.accbal - amount >= 500 and amount <= 20000:
                print("Amount withdrawn successfully")
                break
            else:
                print("Unable to withdraw.")
                attempts += 1
                if attempts == 3:
                    print("Limit exceeded.Too many failed attempts.")
    def balanceEnquiry(self):
        print("Your current balance is:{self.accbal}")
    def validate(self):
        attempts = 0
        while attempts < 3:
            pin = int(input("Enter PIN: "))
            if pin == 1234:
                print("PIN validated successfully!")
                self.viewOptions()
                break
            else:
                print("Invalid PIN.Try again.")
                attempts += 1
        if attempts == 3:
            print("Too many incorrect attempts Exit.")
obj = Bank()
obj.validate()  
obj.deposit()  
obj.withdraw() 
obj.balanceEnquiry() 
