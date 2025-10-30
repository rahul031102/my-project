class BankAccount:
    def __init__(self, name, password, balance=0):
        self.name = name
        self.__password = password  # private attribute
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount, password):
        if password != self.__password:
            print("❌ Incorrect password. Withdrawal denied.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"💸 Withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")

    def check_balance(self, password):
        if password == self.__password:
            print(f"💰 Account balance: ₹{self.balance}")
        else:
            print("❌ Incorrect password. Access denied.")


# ---- Main Program ----
def main():
    print("🏦 Welcome to Simple Bank Account System")
    name = input("Enter your name: ")
    password = input("Set your account password: ")
    account = BankAccount(name, password)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: ₹"))
            account.deposit(amt)

        elif choice == "2":
            amt = float(input("Enter amount to withdraw: ₹"))
            pwd = input("Enter password: ")
            account.withdraw(amt, pwd)

        elif choice == "3":
            pwd = input("Enter password: ")
            account.check_balance(pwd)

        elif choice == "4":
            print("👋 Thank you for using our bank system.")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()