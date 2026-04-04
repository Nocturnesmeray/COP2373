def main():
    """
    Creates and returns the BankAcct class.

    Parameters:
        None

    Variables:
        BankAcct (class): stores the name, account number, amount, and interest rate.
        name (str): Name of the account holder
        account_number (str): Account number
        amount (float): Starting balance
        interest_rate (float): Initial interest rate
        deposit_amount (float): Amount to deposit
        withdraw_amount (float): Amount to withdraw
        new_rate (float): Updated interest rate
        days (int): Number of days for interest calculation
        interest (float): Calculated interest

    Logic:
        1. Define the BankAcct class.
        2. Define the methods to deposit, withdraw, update interest rate, return balance and calculate a new interest rate.

    Return:
        BankAcct (class): stores the name, account number, amount, and interest rate.
    """
    class BankAcct:
        def __init__(self, name, account_number, amount, interest_rate):
            self.name = name
            self.account_number = account_number
            self.amount = amount
            self.interest_rate = interest_rate

        def set_interest_rate(self, new_rate):
            if new_rate > 0:
                self.interest_rate = new_rate
            else:
                print("Interest rate needs to be greater than 0.")

        def deposit(self, deposit_amount):
            if deposit_amount > 0:
                self.amount += deposit_amount
            else:
                print("Deposit amount cannot be negative.")

        def withdraw(self, withdraw_amount):
            if 0 < withdraw_amount <= self.amount:
                self.amount -= withdraw_amount
            else:
                print("Insufficient balance.")

        def balance(self):
            return self.amount

        def calculate_interest(self, days):
            # Calculates an interest rate based on a given number of days.
            return self.amount * self.interest_rate * (days / 365)

        def __str__(self):
            return (f"Account Holder: {self.name} \n"
                    f"Account Number: {self.account_number} \n"
                    f"Balance: {self.amount} \n"
                    f"Interest Rate: {self.interest_rate} \n")

    return BankAcct

def account():
    """
    Tests the methods in the BankAcct class.

    Parameters:
        None

    Variables:
        BankAcct (class): The class returned from main()
        name (str): Name of the account holder
        account_number (str): Account number
        amount (float): Starting balance
        interest_rate (float): Initial interest rate
        acct (object): Instance of BankAcct
        deposit_amount (float): Amount to deposit
        withdraw_amount (float): Amount to withdraw
        new_rate (float): Updated interest rate
        days (int): Number of days for interest calculation
        interest (float): Calculated interest

    Logic:
        1. Ask the user to input account details.
        2. Has the user input information to test the different methods.
        3. Shows the updated account details.

    Return:
        None
    """

    #Has the user give the account details/
    BankAcct = main()
    name = input("Account Holder: ")
    account_number = input("Account Number: ")
    amount = float(input("Starting Balance: "))
    interest_rate = float(input("Interest Rate: "))

    acct = BankAcct(name, account_number, amount, interest_rate)

    deposit_amount = float(input("How much do you want to deposit? "))
    acct.deposit(deposit_amount)
    print(f"After deposit: "
          f"{acct} ")

    withdraw_amount = float(input("How much do you want to withdraw? "))
    acct.withdraw(withdraw_amount)
    print(f"After withdraw: "
          f"{acct} ")

    new_rate = float(input("\nEnter new interest rate: "))
    acct.set_interest_rate(new_rate)
    print("After updating interest rate: ")
    print(acct)

    # Calculate interest based on the amount of days
    days = int(input("\nEnter number of days to calculate interest: "))
    interest = acct.calculate_interest(days)
    print(f"Interest for {days} days: ${interest:.2f}")

if __name__ == "__main__":
    account()

