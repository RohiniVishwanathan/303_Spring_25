import datetime
import string

# ✅ Fixed Caesar Cipher Encoding Function
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)  # List of lowercase letters
    encoded_text = []

    for char in input_text:
        if char.isalpha():
            is_upper = char.isupper()  # Preserve case
            base = ord('A') if is_upper else ord('a')
            encoded_char = chr(((ord(char) - base + shift) % 26) + base)
            encoded_text.append(encoded_char)
        else:
            encoded_text.append(char)  # Keep special characters unchanged

    return (alphabet, "".join(encoded_text))


# ✅ Fixed Caesar Cipher Decoding Function
def decode(input_text, shift):
    decoded_text = []

    for char in input_text:
        if char.isalpha():
            is_upper = char.isupper()  # Preserve case
            base = ord('A') if is_upper else ord('a')
            decoded_char = chr(((ord(char) - base - shift) % 26) + base)
            decoded_text.append(decoded_char)
        else:
            decoded_text.append(char)  # Keep special characters unchanged

    return "".join(decoded_text)


# ✅ Fixed BankAccount Class
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
            raise ValueError("Deposit amount cannot be negative.")  # Proper error handling
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")  # Prevent overdraft
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")

    def view_balance(self):
        return self.balance


# ✅ Fixed SavingsAccount Class (180-day withdrawal restriction)
class SavingsAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        days_since_creation = (datetime.date.today() - self.creation_date).days
        if days_since_creation < 180:
            raise Exception("Withdrawals are only permitted after 180 days.")  # Enforce rule
        if amount > self.balance:
            raise ValueError("Overdrafts are not permitted.")  # No overdrafts

        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")


# ✅ Fixed CheckingAccount Class (Allows overdrafts but applies a $30 fee)
class CheckingAccount(BankAccount):
    def __init__(self, name="Rainy", ID="1234", creation_date=None, balance=0):
        super().__init__(name, ID, creation_date, balance)

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= (amount + 30)  # Apply overdraft fee of $30
            print(f"Overdraft applied! New balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance}")

