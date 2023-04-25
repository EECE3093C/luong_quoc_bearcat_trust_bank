from banking_system import SavingsAccount, CheckingAccount

class Bank:
    """A class representing a bank with various account types."""

    def __init__(self):
        self.accounts = []

   def create_account(self, account_type, account_number, account_holder_name, balance, *args):
        """Creates a new account with the given account type, account number, account holder name, and initial balance.
            Args:
            account_type (str): The account type, either "savings" or "checking".
            account_number (str): The account number.
            account_holder_name (str): The name of the account holder.
            balance (float): The initial balance.
            *args: Additional arguments for account creation (e.g. interest rate or overdraft limit).
        """
        if account_type == "savings":
            account = SavingsAccount(account_number, account_holder_name, balance, *args)
        elif account_type == "checking":
            account = CheckingAccount(account_number, account_holder_name, balance, *args)
        else:
            print("Invalid account type.")
            return
        self.accounts.append(account)

    def delete_account(self, account_number):
        """Deletes an account with the given account number.

        Args:
            account_number (str): The account number of the account to delete.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                return
        print("Account not found.")

    def find_account(self, account_number):
        """Finds an account with the given account number.

        Args:
            account_number (str): The account number to search for.

        Returns:
            Account or None: Returns the account if found, otherwise None.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None

    def list_accounts(self):
        """Displays the details of all accounts."""
        for account in self.accounts:
            account.display()
            print()
