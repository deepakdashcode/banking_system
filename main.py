import sys


class account:
    def __init__(self, name, aadhar, account_number, balance=0):
        self.name = name
        self.aadhar = aadhar
        self.balance = balance
        self.account_number = account_number

    def deposit_money(self, money):
        self.balance = self.balance + money

    def withdraw_money(self, money):
        if self.balance >= money:
            self.balance = self.balance - money
        else:
            error_message = f'Dear {self.name}\nYou have insufficient balance for the task\n'
            sys.stderr.write(error_message)

    def check_balance(self):
        print(self.balance)

    def __str__(self):
        s = f'Name : {self.name}\nAadhar number : {self.aadhar}\nAccount number : {self.account_number}\nBalance : Rs {self.balance}'
        return s



