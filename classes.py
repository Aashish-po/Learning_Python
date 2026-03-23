from datetime import datetime


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


# Test it
laptop = Product("Laptop", 999.99, "Electronics")
mouse = Product("Mouse", 29.99, "Accessories")

print(laptop.name)  # Should print: Laptop
print(laptop.price)  # Should print: 999.99
print(mouse.category)  # Should print: Accessories


# Define the SalesTransaction class here
class SalesTransaction:
    def __init__(self, product_name, quantity, price, date):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.date = date
        self.total = quantity * price


# Test
transaction1 = SalesTransaction("Laptop", 2, 999.99, "2024-01-15")
transaction2 = SalesTransaction("Mouse", 5, 29.99, "2024-01-15")

print(transaction1.total)  # Should print: 1999.98
print(transaction2.total)  # Should print: 149.95


# Define the SalesRecord class here
class SalesRecord:
    def __init__(self, date, product, quantity, price):
        self.date = date
        self.product = product
        self.quantity = quantity
        self.price = price
        # Automatically calculate total
        self.total = quantity * price

    # The __repr__ method provides a string representation of the object for debugging purposes.
    def __repr__(self):
        return f"SalesRecord({self.date}, {self.product}, qty={self.quantity}, ${self.total:.2f})"

    # The __str__ method provides a human-readable string representation of the object.
    def __str__(self):
        return f"{self.date}: {self.product} x{self.quantity} = ${self.total:.2f}"


# Usage
record1 = SalesRecord("2024-01-15", "Laptop", 2, 999.99)
record2 = SalesRecord("2024-01-15", "Mouse", 5, 29.99)

print(record1)  # 2024-01-15: Laptop x2 = $1999.98
print(record2)  # 2024-01-15: Mouse x5 = $149.95

# Access individual attributes
print(f"Product: {record1.product}")
print(f"Total: ${record1.total:.2f}")

# Store multiple records
sales = [
    SalesRecord("2024-01-15", "Laptop", 2, 999.99),
    SalesRecord("2024-01-15", "Mouse", 5, 29.99),
    SalesRecord("2024-01-16", "Keyboard", 3, 79.99),
]

# Calculate total revenue
total_revenue = sum(record.total for record in sales)
print(f"\nTotal Revenue: ${total_revenue:,.2f}")

# Find all laptop sales
laptop_sales = [s for s in sales if s.product == "Laptop"]
print(f"Laptop sales: {len(laptop_sales)}")


# Define the OpenAIConfig class here
class OpenAIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100, temperature=0.7):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.base_url = "https://api.openai.com/v1"

    # The __repr__ method provides a developer-friendly string representation of the object, useful for debugging.
    def __repr__(self):
        return f"OpenAIConfig(model='{self.model}', max_tokens={self.max_tokens})"

    # The __str__ method provides a user-friendly string representation of the object, suitable for display to end-users.
    def __str__(self):
        return f"OpenAI Config: {self.model} (max {self.max_tokens} tokens)"


# Different configurations for different use cases
dev_config = OpenAIConfig(api_key="sk-dev-key", max_tokens=50)

prod_config = OpenAIConfig(
    api_key="sk-prod-key", model="gpt-4", max_tokens=1000, temperature=0.5
)

quick_config = OpenAIConfig("sk-quick-key")  # All defaults

# Use them
print(dev_config)  # OpenAI Config: gpt-3.5-turbo (max 50 tokens)
print(prod_config)  # OpenAI Config: gpt-4 (max 1000 tokens)
print(quick_config)  # OpenAI Config: gpt-3.5-turbo (max 100 tokens)

# Access individual settings
print(f"Dev model: {dev_config.model}")
print(f"Prod temperature: {prod_config.temperature}")

# Store configs in a list for easy management
configs = [dev_config, prod_config, quick_config]


class WeatherData:
    AVERAGE_TEMP = 20.0  # Class variable

    def __init__(self, city, temperature, humidity, date):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.date = date

    # Instance methods to analyze the weather data
    def is_hot(self):
        """Check if temperature is above average."""
        return self.temperature > self.AVERAGE_TEMP

    # The is_cold method checks if the temperature is below the average temperature defined in the class variable AVERAGE_TEMP. It returns True if the temperature is less than AVERAGE_TEMP, indicating that it is cold, and False otherwise.
    def is_cold(self):
        """Check if temperature is below average."""
        return self.temperature < self.AVERAGE_TEMP

    def __str__(self):
        """Human-readable representation."""
        return f"{self.city} on {self.date}: {self.temperature}°C, {self.humidity}% humidity"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"WeatherData('{self.city}', {self.temperature}, {self.humidity}, '{self.date}')"


# Test
weather1 = WeatherData("Kathmandu", 25, 65, "2024-03-20")
weather2 = WeatherData("Pokhara", 18, 70, "2024-03-20")

print(weather1)  # Kathmandu on 2024-03-20: 25°C, 65% humidity
print(weather2)  # Pokhara on 2024-03-20: 18°C, 70% humidity

print(f"Is it hot in Kathmandu? {weather1.is_hot()}")  # True
print(f"Is it hot in Pokhara? {weather2.is_hot()}")  # False


# Each account has its own data, so we can create multiple accounts without them interfering with each other.
# Define the BankAccount class here
class BankAccount1:
    def __init__(self, owner, balance=0):
        self.owner = owner  # Each account has its own owner
        self.balance = balance  # Each account has its own balance
        self.transactions = []  # Each account has its own transaction history


# Create different accounts
account1 = BankAccount1("Aashish", 1000)
account2 = BankAccount1("Alice", 500)

# Each has independent data
print(account1.balance)  # 1000
print(account2.balance)  # 500

# Changing one doesn't affect the other
account1.balance += 200
print(account1.balance)  # 1200
print(account2.balance)  # 500 (unchanged)


# Class attributes are shared across all instances, so they can be used to store information that is common to all accounts, such as the bank name or interest rate.
# Define the BankAccount class with class attributes here
class BankAccount2:
    # Class attributes - same for ALL accounts
    bank_name = "Nepal Bank"
    interest_rate = 0.05
    total_accounts = 0

    def __init__(self, owner, balance=0):
        # Instance attributes - unique to each account
        self.owner = owner
        self.balance = balance

        # Increment class attribute
        BankAccount2.total_accounts += 1


# Create accounts
account1 = BankAccount2("Aashish", 1000)
account2 = BankAccount2("Alice", 500)

# Class attributes are shared
print(account1.bank_name)  # Nepal Bank
print(account2.bank_name)  # Nepal Bank (same)

# Total accounts incremented for each new account
print(BankAccount2.total_accounts)  # 2

# Access via class or instance
print(account1.interest_rate)  # 0.05
print(BankAccount2.interest_rate)  # 0.05 (same)


# This class demonstrates instance methods that operate on instance attributes (like result) and return values for chaining.
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self  # Return for chaining

    def subtract(self, number):
        self.result -= number
        return self

    def get_result(self):
        return self.result

    def reset(self):
        self.result = 0


# Usage
calc = Calculator()
calc.add(10)  # self is passed automatically
calc.add(5)  # result = 15
calc.subtract(3)  # result = 12

print(calc.get_result())  # 12

# Method chaining (because methods return self)
result = Calculator().add(10).subtract(3).get_result()
print(result)  # 7


# This class represents a product with methods to calculate price with tax, manage stock, and sell products. It demonstrates the use of class attributes (tax_rate) and instance methods that operate on instance attributes (name, price, stock).
class product1:
    # Class attribute
    tax_rate = 0.13  # 13% VAT in Nepal

    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    # Instance method to calculate price with tax
    def get_price_with_tax(self):
        return self.price * (1 + self.tax_rate)

    # Instance method to add stock
    def add_stock(self, quantity):
        self.stock += quantity

    # Instance method to sell products, reducing stock
    def sell(self, quantity):
        if quantity > self.stock:
            print(f"Not enough stock to sell {quantity} units of {self.name}.")
            return False
        self.stock -= quantity
        return True

    # Instance method to check if product is in stock
    def is_in_stock(self):
        if self.stock <= 0:
            print(f"{self.name} is out of stock.")
            return False
        return self.stock > 0

    # The __repr__ method provides a developer-friendly string representation of the object, useful for debugging.
    def __repr__(self):
        return f"product1('{self.name}', {self.price}, stock={self.stock})"

    # The __str__ method provides a human-readable string representation of the object, suitable for display to end-users.
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"


# Test it
laptop = product1("Laptop", 80000, stock=5)
print(laptop.get_price_with_tax())  # Should calculate with tax
laptop.sell(2)
print(laptop.stock)  # Should be 3


# This class represents a bank account with methods for depositing, withdrawing, calculating interest, and printing statements.
class BankAccount:
    """Represent a bank account with transaction methods."""

    # Class attributes
    bank_name = "Nepal Bank"
    interest_rate = 0.05
    min_balance = 500

    def __init__(self, owner, account_number, balance=0):
        """Initialize account."""
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

        # Record initial deposit
        if balance > 0:
            self._record_transaction("Initial Deposit", balance)

    def _record_transaction(self, transaction_type, amount):
        """Private method to record transaction."""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.transaction_history.append(transaction)

    def deposit(self, amount):
        """Deposit money."""
        if amount <= 0:
            print("❌ Deposit amount must be positive")
            return False

        self.balance += amount
        self._record_transaction("Deposit", amount)
        print(f"✅ Deposited Rs. {amount:,.2f}. New balance: Rs. {self.balance:,.2f}")
        return True

    def withdraw(self, amount):
        """Withdraw money."""
        if amount <= 0:
            print("❌ Withdrawal amount must be positive")
            return False

        # Check minimum balance requirement
        if self.balance - amount < self.min_balance:
            print(
                f"❌ Insufficient funds. Minimum balance Rs. {self.min_balance:,.2f} required"
            )
            print(
                f"   Available for withdrawal: Rs. {self.balance - self.min_balance:,.2f}"
            )
            return False

        self.balance -= amount
        self._record_transaction("Withdrawal", -amount)
        print(f"✅ Withdrew Rs. {amount:,.2f}. New balance: Rs. {self.balance:,.2f}")
        return True

    def get_balance(self):
        """Get current balance."""
        return self.balance

    def calculate_interest(self):
        """Calculate annual interest earned."""
        interest = self.balance * self.interest_rate
        return interest

    def apply_interest(self):
        """Apply interest to account."""
        interest = self.calculate_interest()
        self.balance += interest
        self._record_transaction("Interest", interest)
        print(
            f"✅ Interest applied: Rs. {interest:,.2f}. New balance: Rs. {self.balance:,.2f}"
        )
        return interest

    def get_transaction_history(self):
        """Get all transactions."""
        return self.transaction_history

    def print_statement(self):
        """Print account statement."""
        print("=" * 70)
        print(f"{self.bank_name} - Account Statement")
        print("=" * 70)
        print(f"Account Holder: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: Rs. {self.balance:,.2f}")
        print("\nTransaction History:")
        print("-" * 70)
        print(f"{'Date':<20} {'Type':<15} {'Amount':>15} {'Balance':>15}")
        print("-" * 70)

        for txn in self.transaction_history:
            amount_str = f"Rs. {abs(txn['amount']):,.2f}"
            if txn["amount"] < 0:
                amount_str = f"-{amount_str}"

            print(
                f"{txn['timestamp']:<20} {txn['type']:<15} {amount_str:>15} Rs. {txn['balance']:>12,.2f}"
            )

        print("=" * 70)

    def __str__(self):
        """String representation."""
        return f"{self.bank_name} Account: {self.account_number} ({self.owner}) - Balance: Rs. {self.balance:,.2f}"

    def __repr__(self):
        """Developer representation."""
        return f"BankAccount('{self.owner}', '{self.account_number}', {self.balance})"


# %%
account = BankAccount("Aashish Poudel", "NB-001", 10000)
print(account)

# %%
