"""
reader_test.py

A simple Python file designed for testing a code reader.

This file intentionally contains many lines of ordinary Python code.
It includes:
- Variables
- Functions
- Classes
- Lists
- Dictionaries
- Loops
- Conditions
- File handling
- Simple calculations
- Text processing
- A small menu program

No external packages are required.
"""


# ============================================================
# PAGE 1 - BASIC VARIABLES
# ============================================================

APP_NAME = "Reader Test Program"
VERSION = "1.0"
AUTHOR = "Example Author"

user_name = "Alex"
user_age = 28
user_score = 95.5
is_active = True

favorite_colors = [
    "blue",
    "green",
    "orange",
    "purple",
    "red",
]

print("Application:", APP_NAME)
print("Version:", VERSION)
print("Author:", AUTHOR)
print("User:", user_name)
print("Age:", user_age)
print("Score:", user_score)
print("Active:", is_active)

print()
print("Favorite colors:")

for color in favorite_colors:
    print("-", color)


# ============================================================
# PAGE 2 - SIMPLE FUNCTIONS
# ============================================================

def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def add_numbers(first, second):
    """Add two numbers."""
    return first + second


def subtract_numbers(first, second):
    """Subtract the second number from the first."""
    return first - second


def multiply_numbers(first, second):
    """Multiply two numbers."""
    return first * second


def divide_numbers(first, second):
    """Divide two numbers safely."""
    if second == 0:
        return None

    return first / second


def square(number):
    """Return the square of a number."""
    return number * number


def is_even(number):
    """Return True when a number is even."""
    return number % 2 == 0


print()
print(greet("Reader"))

a = 20
b = 5

print("Addition:", add_numbers(a, b))
print("Subtraction:", subtract_numbers(a, b))
print("Multiplication:", multiply_numbers(a, b))
print("Division:", divide_numbers(a, b))
print("Square:", square(a))
print("Is even:", is_even(a))


# ============================================================
# PAGE 3 - CONDITIONS
# ============================================================

def describe_number(number):
    """Return a description of a number."""

    if number > 100:
        return "The number is greater than 100."

    if number == 100:
        return "The number is exactly 100."

    if number > 50:
        return "The number is greater than 50."

    if number > 0:
        return "The number is positive."

    if number == 0:
        return "The number is zero."

    return "The number is negative."


numbers_to_test = [
    150,
    100,
    75,
    25,
    0,
    -10,
]

for number in numbers_to_test:
    description = describe_number(number)
    print(number, "->", description)


def get_grade(score):
    """Convert a score into a simple letter grade."""

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"


scores = [95, 87, 76, 64, 45]

print()
print("Grades:")

for score in scores:
    grade = get_grade(score)
    print(score, "=", grade)


# ============================================================
# PAGE 4 - LISTS AND LOOPS
# ============================================================

fruits = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "pear",
    "watermelon",
]

print()
print("Fruit list:")

for index, fruit in enumerate(fruits):
    print(index, fruit)


print()
print("Uppercase fruits:")

for fruit in fruits:
    print(fruit.upper())


print()
print("Fruit lengths:")

for fruit in fruits:
    length = len(fruit)
    print(fruit, "has", length, "letters")


numbers = list(range(1, 21))

print()
print("Numbers from 1 to 20:")

for number in numbers:
    print(number)


print()
print("Even numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number)


print()
print("Odd numbers:")

for number in numbers:
    if number % 2 != 0:
        print(number)


# ============================================================
# PAGE 5 - LIST OPERATIONS
# ============================================================

shopping_list = [
    "bread",
    "milk",
    "eggs",
]

shopping_list.append("cheese")
shopping_list.append("apples")

print()
print("Shopping list:", shopping_list)

if "milk" in shopping_list:
    print("Milk is on the list.")

if "coffee" not in shopping_list:
    print("Coffee is not on the list.")


shopping_list.remove("bread")

print()
print("After removing bread:")
print(shopping_list)


shopping_list.insert(0, "water")

print()
print("After adding water at the beginning:")
print(shopping_list)


sorted_items = sorted(shopping_list)

print()
print("Sorted items:")

for item in sorted_items:
    print(item)


numbers = [5, 2, 9, 1, 7, 3, 8, 4, 6]

print()
print("Original numbers:", numbers)

numbers.sort()

print("Sorted numbers:", numbers)

numbers.reverse()

print("Reversed numbers:", numbers)


# ============================================================
# PAGE 6 - DICTIONARIES
# ============================================================

person = {
    "name": "Alex",
    "age": 28,
    "city": "London",
    "job": "Developer",
    "active": True,
}

print()
print("Person information:")

for key, value in person.items():
    print(key, ":", value)


print()
print("Name:", person["name"])
print("City:", person["city"])


person["age"] = 29
person["job"] = "Senior Developer"

print()
print("Updated person:")

for key, value in person.items():
    print(key, ":", value)


people = {
    "alice": {
        "age": 25,
        "city": "London",
    },
    "bob": {
        "age": 31,
        "city": "Manchester",
    },
    "charlie": {
        "age": 22,
        "city": "Bristol",
    },
}


print()
print("People:")

for name, information in people.items():
    print(
        name,
        "is",
        information["age"],
        "years old and lives in",
        information["city"],
    )


# ============================================================
# PAGE 7 - TUPLES AND SETS
# ============================================================

coordinates = (51.5074, -0.1278)

print()
print("Coordinates:")
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])


dimensions = (1920, 1080)

width = dimensions[0]
height = dimensions[1]

print()
print("Screen width:", width)
print("Screen height:", height)


colors = {
    "red",
    "green",
    "blue",
    "red",
    "blue",
}

print()
print("Unique colors:")

for color in colors:
    print(color)


first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8}

print()
print("Set operations")
print("First:", first_set)
print("Second:", second_set)
print("Union:", first_set | second_set)
print("Intersection:", first_set & second_set)
print("Difference:", first_set - second_set)


# ============================================================
# PAGE 8 - WHILE LOOPS
# ============================================================

counter = 1

print()
print("Counting with a while loop:")

while counter <= 10:
    print("Counter:", counter)
    counter += 1


print()
print("Countdown:")

countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Go!")


def countdown_message(start):
    """Create a countdown message."""

    messages = []

    number = start

    while number > 0:
        messages.append(f"{number}...")
        number -= 1

    messages.append("Finished!")

    return messages


print()
for message in countdown_message(5):
    print(message)


# ============================================================
# PAGE 9 - STRING OPERATIONS
# ============================================================

text = "Python is a simple and powerful programming language."

print()
print("Original text:")
print(text)

print()
print("Lowercase:")
print(text.lower())

print()
print("Uppercase:")
print(text.upper())

print()
print("Length:")
print(len(text))

print()
print("Words:")

words = text.split()

for word in words:
    print(word)


sentence = "one,two,three,four,five"

parts = sentence.split(",")

print()
print("Split sentence:")

for part in parts:
    print(part)


joined = " | ".join(parts)

print()
print("Joined again:")
print(joined)


message = "Hello, Reader!"

print()
print(message.replace("Reader", "Python"))


# ============================================================
# PAGE 10 - STRING FORMATTING
# ============================================================

name = "Jordan"
age = 34
city = "London"

message = f"My name is {name}."
print(message)

message = f"I am {age} years old."
print(message)

message = f"I live in {city}."
print(message)

message = (
    f"My name is {name}, "
    f"I am {age} years old, "
    f"and I live in {city}."
)

print(message)


price = 19.99
quantity = 3

total = price * quantity

print()
print(f"Price: £{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: £{total:.2f}")


percentage = 0.875

print()
print(f"Percentage: {percentage:.1%}")


# ============================================================
# PAGE 11 - LIST COMPREHENSIONS
# ============================================================

numbers = list(range(1, 11))

squares = [
    number * number
    for number in numbers
]

print()
print("Squares:")
print(squares)


even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print()
print("Even numbers:")
print(even_numbers)


odd_numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print()
print("Odd numbers:")
print(odd_numbers)


words = [
    "python",
    "reader",
    "testing",
    "code",
    "example",
]

long_words = [
    word
    for word in words
    if len(word) > 5
]

print()
print("Long words:")
print(long_words)


uppercase_words = [
    word.upper()
    for word in words
]

print()
print("Uppercase words:")
print(uppercase_words)


# ============================================================
# PAGE 12 - ERROR HANDLING
# ============================================================

def safe_integer(value):
    """Try to convert a value into an integer."""

    try:
        return int(value)

    except ValueError:
        print("Could not convert:", value)
        return None


values = [
    "10",
    "25",
    "hello",
    "50",
    "100",
]

print()
print("Converting values:")

for value in values:
    result = safe_integer(value)
    print(value, "->", result)


def safe_division(first, second):
    """Perform division with basic error handling."""

    try:
        result = first / second
        return result

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

    except TypeError:
        print("Invalid values.")
        return None


print()
print("Safe division:")
print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division("10", 2))


# ============================================================
# PAGE 13 - A SIMPLE CLASS
# ============================================================

class Person:
    """A simple person class."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Return an introduction."""

        return (
            f"Hello, my name is {self.name} "
            f"and I am {self.age} years old."
        )

    def have_birthday(self):
        """Increase the person's age."""

        self.age += 1


person_one = Person("Alice", 25)
person_two = Person("Bob", 31)

print()
print(person_one.introduce())
print(person_two.introduce())

person_one.have_birthday()

print()
print("After birthday:")
print(person_one.introduce())


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def description(self):
        return (
            f"Rectangle {self.width} x {self.height}, "
            f"area={self.area()}, "
            f"perimeter={self.perimeter()}"
        )


rectangle = Rectangle(10, 5)

print()
print(rectangle.description())


# ============================================================
# PAGE 14 - ANOTHER CLASS
# ============================================================

class BankAccount:
    """A very small bank account example."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""

        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount):
        """Remove money if enough balance exists."""

        if amount <= 0:
            return False

        if amount > self.balance:
            return False

        self.balance -= amount
        return True

    def show_balance(self):
        """Return the current balance."""

        return f"{self.owner}: £{self.balance:.2f}"


account = BankAccount("Taylor", 100)

print()
print(account.show_balance())

account.deposit(50)

print(account.show_balance())

account.withdraw(25)

print(account.show_balance())

success = account.withdraw(500)

if success:
    print("Withdrawal successful.")
else:
    print("Withdrawal failed.")


# ============================================================
# PAGE 15 - FILE HANDLING
# ============================================================

sample_filename = "reader_sample.txt"

sample_lines = [
    "This is a sample file.",
    "It is created by the Python test program.",
    "The purpose is to demonstrate file handling.",
    "Reading and writing files is common in Python.",
]

try:
    with open(sample_filename, "w", encoding="utf-8") as file:
        for line in sample_lines:
            file.write(line + "\n")

    print()
    print("Sample file written successfully.")

except OSError as error:
    print("Could not write file:", error)


try:
    with open(sample_filename, "r", encoding="utf-8") as file:
        contents = file.read()

    print()
    print("File contents:")
    print(contents)

except OSError as error:
    print("Could not read file:", error)


# ============================================================
# PAGE 16 - FUNCTIONS WITH DEFAULT VALUES
# ============================================================

def create_user(
    name,
    age=18,
    city="Unknown",
    active=True,
):
    """Create a dictionary containing user information."""

    return {
        "name": name,
        "age": age,
        "city": city,
        "active": active,
    }


user_a = create_user("Sam")
user_b = create_user("Jamie", 30)
user_c = create_user(
    "Morgan",
    42,
    "London",
    False,
)

print()
print("Created users:")

print(user_a)
print(user_b)
print(user_c)


def calculate_total(
    price,
    quantity=1,
    discount=0,
):
    """Calculate a final price."""

    subtotal = price * quantity
    discount_amount = subtotal * discount
    final_price = subtotal - discount_amount

    return final_price


print()
print("Totals:")

print(calculate_total(10))
print(calculate_total(10, 3))
print(calculate_total(100, 2, 0.10))


# ============================================================
# PAGE 17 - SIMPLE DATA PROCESSING
# ============================================================

products = [
    {
        "name": "Notebook",
        "price": 4.50,
        "stock": 20,
    },
    {
        "name": "Pen",
        "price": 1.20,
        "stock": 100,
    },
    {
        "name": "Backpack",
        "price": 35.00,
        "stock": 8,
    },
    {
        "name": "Bottle",
        "price": 12.50,
        "stock": 15,
    },
]


print()
print("Product catalog:")

for product in products:
    print(
        product["name"],
        "-",
        f"£{product['price']:.2f}",
        "-",
        product["stock"],
        "in stock",
    )


total_stock = 0

for product in products:
    total_stock += product["stock"]

print()
print("Total stock:", total_stock)


total_value = 0

for product in products:
    value = product["price"] * product["stock"]
    total_value += value

print(f"Total inventory value: £{total_value:.2f}")


expensive_products = []

for product in products:
    if product["price"] >= 10:
        expensive_products.append(product)


print()
print("Products costing £10 or more:")

for product in expensive_products:
    print(product["name"])


# ============================================================
# PAGE 18 - SIMPLE SEARCH FUNCTIONS
# ============================================================

def find_product(products, name):
    """Find a product by name."""

    for product in products:
        if product["name"].lower() == name.lower():
            return product

    return None


def find_products_under_price(products, maximum_price):
    """Find products below a maximum price."""

    results = []

    for product in products:
        if product["price"] <= maximum_price:
            results.append(product)

    return results


search_result = find_product(products, "Notebook")

print()
print("Search result:")

if search_result is not None:
    print(search_result)
else:
    print("Product not found.")


cheap_products = find_products_under_price(
    products,
    10,
)

print()
print("Products under £10:")

for product in cheap_products:
    print(
        product["name"],
        f"£{product['price']:.2f}",
    )


# ============================================================
# PAGE 19 - A SMALL TEXT MENU
# ============================================================

def print_menu():
    """Display the application menu."""

    print()
    print("=" * 40)
    print("READER TEST MENU")
    print("=" * 40)
    print("1. Say hello")
    print("2. Show numbers")
    print("3. Show products")
    print("4. Show information")
    print("5. Exit")
    print("=" * 40)


def show_numbers():
    """Display a small list of numbers."""

    print()
    print("Numbers:")

    for number in range(1, 11):
        print(f"Number {number}")


def show_products():
    """Display all products."""

    print()
    print("Products:")

    for product in products:
        print(
            f"- {product['name']}: "
            f"£{product['price']:.2f}"
        )


def show_information():
    """Display application information."""

    print()
    print("Application information")
    print("-----------------------")
    print("Name:", APP_NAME)
    print("Version:", VERSION)
    print("Author:", AUTHOR)


def run_demo_menu():
    """
    Run a non-interactive demonstration of the menu.

    This function does not call input(), which makes it
    convenient for automated reader and test environments.
    """

    print_menu()

    print()
    print("Demonstrating menu option 1:")
    print(greet("Reader"))

    print()
    print("Demonstrating menu option 2:")
    show_numbers()

    print()
    print("Demonstrating menu option 3:")
    show_products()

    print()
    print("Demonstrating menu option 4:")
    show_information()


# ============================================================
# PAGE 20 - FINAL TESTS
# ============================================================

def run_final_tests():
    """Run several small tests."""

    print()
    print("=" * 50)
    print("FINAL TESTS")
    print("=" * 50)

    test_one = add_numbers(2, 3)

    if test_one == 5:
        print("Test 1: PASS")
    else:
        print("Test 1: FAIL")

    test_two = multiply_numbers(4, 5)

    if test_two == 20:
        print("Test 2: PASS")
    else:
        print("Test 2: FAIL")

    test_three = square(6)

    if test_three == 36:
        print("Test 3: PASS")
    else:
        print("Test 3: FAIL")

    test_four = is_even(10)

    if test_four:
        print("Test 4: PASS")
    else:
        print("Test 4: FAIL")

    test_five = get_grade(95)

    if test_five == "A":
        print("Test 5: PASS")
    else:
        print("Test 5: FAIL")

    test_six = find_product(products, "Pen")

    if test_six is not None:
        print("Test 6: PASS")
    else:
        print("Test 6: FAIL")

    print("=" * 50)
    print("TESTS COMPLETE")
    print("=" * 50)


def main():
    """Main entry point for the program."""

    print()
    print("*" * 50)
    print("WELCOME TO THE PYTHON READER TEST")
    print("*" * 50)

    print()
    print("This file contains many examples of Python code.")
    print("It is intended for testing a code reader.")
    print("No external libraries are required.")

    run_demo_menu()
    run_final_tests()

    print()
    print("Program finished.")
    print("Thank you for testing the reader.")


if __name__ == "__main__":
    main()
