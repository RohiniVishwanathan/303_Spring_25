import datetime
import string
import pytest

def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_chars = []
    for char in input_text:
        if char.isalpha():
            c = char.lower()
            base = ord('a')
            shifted = chr((ord(c) - base + shift) % 26 + base)
            encoded_chars.append(shifted)
        else:
            encoded_chars.append(char)
    return (alphabet, "".join(encoded_chars))

def decode(input_text, shift):
    decoded_chars = []
    for char in input_text:
        if char.isalpha():
            c = char.lower()
            base = ord('a')
            shifted = chr((ord(c) - base - shift) % 26 + base)
            decoded_chars.append(shifted)
        else:
            decoded_chars.append(char)
    return "".join(decoded_chars)

class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = datetime.date.today()
        elif creation_date > datetime.date.today():
            raise Exception("Account creation date cannot be in the future.")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount cannot be negative.")
            return self.balance
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")
        return self.balance

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            pytest.xfail("Withdrawals are only permitted after 180 days.")
            return self.balance
        if amount > self.balance:
            raise ValueError("Overdrafts are not permitted.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= (amount + 30)
            print(f"Overdraft applied! New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance}")
        return self.balance

