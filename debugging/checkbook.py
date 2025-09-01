class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance tracking.
    """

    def __init__(self):
        """
        Initialize the checkbook with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Args:
            amount (float): The amount to deposit.

        Effects:
            Increases the balance and prints the transaction details.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook.

        Args:
            amount (float): The amount to withdraw.

        Effects:
            Decreases the balance if funds are sufficient and prints transaction details.
            If insufficient funds, prints an error message.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Print the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop of the program. Allows the user to interact with the Checkbook
    through a text-based menu.
    """
    cb = Checkbook()

    while True:
        # Prompt user for an action
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            # Exit the program
            break
        elif action.lower() == 'deposit':
            # Prompt user for deposit amount and call deposit method
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            # Prompt user for withdrawal amount and call withdraw method
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Please enter a positive amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action.lower() == 'balance':
            # Show the current balance
            cb.get_balance()
        else:
            # Handle unrecognized input
            print("Invalid command. Please try again.")

# Ensure the main loop runs only if the script is executed directly
if __name__ == "__main__":
    main()
