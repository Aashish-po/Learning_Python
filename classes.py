# Define the Product class here
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
