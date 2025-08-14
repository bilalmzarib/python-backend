# Exercise 1: Basic Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1.introduce())
print(p2.introduce())

# ------------------------------------------------------------

# Exercise 2: Instance vs Class Variables
class Dog:
    species = "Canis familiaris" 

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}. Species: {self.species}."

d1 = Dog("Rex", "Labrador")
d2 = Dog("Bella", "Beagle")
print(d1.describe())
print(d2.describe())

# Modify species for d1 instance only
d1.species = "Canis lupus"
print("After modifying species for d1:")
print(d1.describe())
print(d2.describe())

# Exercise 3: Bank Account with Validation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

acc = BankAccount("John")
acc.deposit(500)
acc.withdraw(100)
acc.withdraw(1000)
print(f"{acc.account_holder}'s balance: ${acc.get_balance()}")

# Exercise 4: Library System
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def list_books(self):
        return [book.display_info() for book in self.books]

library = Library()
book1 = Book("1984", "George Orwell", "123")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "456")

library.add_book(book1)
library.add_book(book2)
print("Books in library:")
for info in library.list_books():
    print(info)

library.remove_book("123")
print("After removing one book:")
for info in library.list_books():
    print(info)

# Exercise 5: Class Variable Counter
class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    def display_car(self):
        return f"{self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
print(car1.display_car())
print(car2.display_car())
print("Total cars created:", Car.get_total_cars())

# Exercise 6: Student Grade Tracker
class Student:
    school_name = "Greenwood High"

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def student_info(self):
        avg = self.average_grade()
        return f"Name: {self.name}, School: {Student.school_name}, Average Grade: {avg:.2f}"

stu = Student("Emily")
stu.add_grade(90)
stu.add_grade(85)
stu.add_grade(105)
print(stu.student_info())

# Exercise 7: Restaurant Order System
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        return f"{self.category} - {self.name}: ${self.price:.2f}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def display_order(self):
        for item in self.items:
            print(item.display())
        print(f"Total: ${self.calculate_total():.2f}")

menu1 = MenuItem("Spring Rolls", 5.99, "Appetizer")
menu2 = MenuItem("Steak", 18.99, "Main Course")
menu3 = MenuItem("Ice Cream", 4.50, "Dessert")

order = Order()
order.add_item(menu1)
order.add_item(menu2)
order.add_item(menu3)
order.display_order()

order.remove_item("Steak")
print("\nAfter removing Steak:")
order.display_order()
