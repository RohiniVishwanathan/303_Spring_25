import datetime
import string

def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = []

    for char in input_text:
        if char.isalpha():
            base = ord('a')  # Convert everything to lowercase
            encoded_char = chr(((ord(char.lower()) - base + shift) % 26) + base)
            encoded_text.append(encoded_char)
        else:
            encoded_text.append(char)

    return (alphabet, "".join(encoded_text))

def decode(input_text, shift):
    decoded_text = []

    for char in input_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded_char = chr(((ord(char) - base - shift) % 26) + base)
            decoded_text.append(decoded_char)
        else:
            decoded_text.append(char)

    return "".join(decoded_text)

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
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")

    def view_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            raise Exception("Withdrawals are only permitted after 180 days.")
        if amount > self.balance:
            raise ValueError("Overdrafts are not permitted.")

        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")

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

