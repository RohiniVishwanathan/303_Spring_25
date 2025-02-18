import datetime
import string

# Function to encode using Caesar Cipher
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""
    
    for char in input_text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = alphabet[(alphabet.index(char.lower()) + shift) % 26]
            encoded_text += shifted_char.upper() if is_upper else shifted_char
        else:
            encoded_text += char
    
    return (alphabet, encoded_text)

# Function to decode using Caesar Cipher
def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ""
    
    for char in input_text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = alphabet[(alphabet.index(char.lower()) - shift) % 26]
            decoded_text += shifted_char.upper() if is_upper else shifted_char
        else:
            decoded_text += char
    
    return decoded_text

# BankAccount class
class BankAccount:
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        if creation_date is None:
            creation_date = datetime.date.today()
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")
        
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print(f"New balance after deposit: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"New balance after withdrawal: {self.balance}")

    def view_balance(self):
        return self.balance

# SavingsAccount subclass
class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            raise Exception("Withdrawals are only permitted after 180 days.")
        if self.balance - amount < 0:
            raise Exception("Overdrafts are not permitted.")
        super().withdraw(amount)

# CheckingAccount subclass
class CheckingAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 30  # Overdraft fee
            print("Overdraft fee of $30 applied.")
        print(f"New balance after withdrawal: {self.balance}")

