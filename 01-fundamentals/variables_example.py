"""
Variables and Data Types Example

Demonstrates Python's dynamic typing and various data types.
"""


def demonstrate_variables():
    """Show different variable types and operations."""
    print("=" * 60)
    print("VARIABLES AND DATA TYPES")
    print("=" * 60)

    # Integer
    age = 18
    print(f"\nInteger: age = {age}, type = {type(age)}")

    # Float
    height = 5.8
    print(f"Float: height = {height}, type = {type(height)}")

    # String
    name = "Aashish"
    print(f"String: name = '{name}', type = {type(name)}")

    # Boolean
    is_student = True
    print(f"Boolean: is_student = {is_student}, type = {type(is_student)}")

    # List
    numbers = [1, 2, 3, 4, 5]
    print(f"List: numbers = {numbers}, type = {type(numbers)}")

    # Dictionary
    person = {"name": "Aashish", "age": 18}
    print(f"Dict: person = {person}, type = {type(person)}")

    print("\n" + "=" * 60)


def demonstrate_type_conversion():
    """Show type conversion examples."""
    print("\nTYPE CONVERSION")
    print("=" * 60)

    # String to int
    age_str = "18"
    age_int = int(age_str)
    print(f"str to int: '{age_str}' → {age_int}")

    # Int to string
    number = 42
    number_str = str(number)
    print(f"int to str: {number} → '{number_str}'")

    # String to float
    price_str = "19.99"
    price_float = float(price_str)
    print(f"str to float: '{price_str}' → {price_float}")

    # Int to bool
    print(f"int to bool: 0 → {bool(0)}, 1 → {bool(1)}")

    print("=" * 60)


def demonstrate_scope():
    """Show variable scope."""
    print("\nVARIABLE SCOPE")
    print("=" * 60)

    global_var = "I'm global"

    def inner_function():
        local_var = "I'm local"
        print(f"Inside function: {local_var}")
        print(f"Can access global: {global_var}")

    inner_function()
    print(f"Outside function: {global_var}")
    # print(local_var)  # Would cause NameError

    print("=" * 60)


if __name__ == "__main__":
    demonstrate_variables()
    demonstrate_type_conversion()
    demonstrate_scope()

    print("\n✓ Examples complete!")
