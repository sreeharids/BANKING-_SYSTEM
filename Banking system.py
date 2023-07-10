class BankAccount:
    def __init__(self, account_number, pin, account_holder_name, account_holder_number, account_holder_address):
        self.account_number = account_number
        self.pin = pin
        self.account_holder_name = account_holder_name
        self.account_holder_number = account_holder_number
        self.account_holder_address = account_holder_address
        self.balance = 0

    def login(self):
        entered_account_number = input("Enter account number: ")
        entered_pin = input("Enter PIN: ")

        if entered_account_number == self.account_number and entered_pin == self.pin:
            print("Login successful!")
            return True
        else:
            print("Invalid account number or PIN.")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount} deposited successfully.")
            print(f"Current balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Amount {amount} withdrawn successfully.")
                print(f"Current balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount.")


# Creating a bank account
account_number = input(" Enter your Account number:  ")
pin = input("Enter pin:  ")
account_holder_name =input("Enter your name:  ")
account_holder_number =input("Enter your phone number:  ")
account_holder_address =input("Enter your Address:  ")
bank_account = BankAccount(account_number, pin, account_holder_name, account_holder_number, account_holder_address)
print("your Account is created Sucessfully! ")
print ( """Now you can Enjoy Banking facilitys """)
# Account login
while True:
    if bank_account.login():
        break

# Performing transactions
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        bank_account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        bank_account.withdraw(amount)
    elif choice == "3":
        print("Thank you for using our banking system. Goodbye!")
        break
    else:
        print("Invalid Option.")
