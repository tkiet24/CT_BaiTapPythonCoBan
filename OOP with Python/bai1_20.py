import json
import math
from abc import ABC, abstractmethod
from datetime import datetime

# 1. Lớp đơn giản – Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def getInfo(self):
        return f"{self.year} {self.make} {self.model}"

# 2. Khởi tạo & Phương thức – BankAccount
class BankAccount:
    def __init__(self, accountNumber, owner, balance=0):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def getBalance(self):
        return self.balance

# 3. Đóng gói & Kiểm tra – Student
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = None # Thuộc tính riêng tư

    def setGrade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def getGrade(self):
        return self.__grade

# 4. Kế thừa đơn – Vehicle và Bus
class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, maxSpeed, mileage, passengers):
        super().__init__(maxSpeed, mileage)
        self.passengers = passengers

# 5. Phương thức lớp & tĩnh – Robot
class Robot:
    activeCount = 0 # Class attribute

    def __init__(self, name):
        self.name = name
        Robot.activeCount += 1
        self.isActive = True

    def remove(self):
        if self.isActive:
            self.isActive = False
            Robot.activeCount -= 1

    @classmethod
    def numberActive(cls):
        print(f"Active robots: {cls.activeCount}")

# 6. Đa hình – Shape / Circle / Rectangle
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method area")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# 7. ToString / str – Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

# 8. Operator overloading – Vector2D
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        newX = self.x + other.x
        newY = self.y + other.y
        return Vector2D(newX, newY)
    
    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

# 9. Composition – Employee và Salary
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

class Employee:
    def __init__(self, name, salaryObj):
        self.name = name
        self.salary = salaryObj # Composition: Employee HAS-A Salary

    def totalCompensation(self):
        return self.salary.pay + self.salary.bonus

# 10. Multiple inheritance – Logger và FileWriter
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class FileWriter:
    def write(self, text):
        print(f"[WRITE] {text}")

class LogFileWriter(Logger, FileWriter):
    def processLog(self, message):
        # Sử dụng write để log
        self.write(f"LOGGING: {message}") 

# 11. Singleton class – DatabaseConnection
class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name="default"):
        # Ngăn __init__ chạy lại nhiều lần nếu instance đã tồn tại
        if not hasattr(self, 'initialized'):
            self.dbName = db_name
            self.initialized = True
            
    @classmethod
    def getInstance(cls):
        return cls._instance

# 12. Abstract base class – AbstractAnimal
class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Woof!"

# 13. Kế thừa đa cấp – Employee / Manager / Executive
class EmployeeBase:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(EmployeeBase):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Executive(Manager):
    def __init__(self, name, salary, department, stockOptions):
        super().__init__(name, salary, department)
        self.stockOptions = stockOptions

# 14. Mixin class – JsonSerializableMixin
class JsonSerializableMixin:
    def toJson(self):
        # Sử dụng __dict__ để lấy tất cả thuộc tính của instance
        return json.dumps(self.__dict__, indent=4)

class Product(JsonSerializableMixin):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# 15. Encapsulation & Property decorator – Circle
class Circle:
    def __init__(self, radius):
        self._radius = radius # Thuộc tính riêng tư

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative.")

    def area(self):
        return math.pi * (self._radius ** 2)

# 16. Library System – Book / Library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available" # available/borrowed

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def borrowBook(self, title):
        for book in self.books:
            if book.title == title and book.status == "available":
                book.status = "borrowed"
                return f"'{title}' has been borrowed."
        return f"Book '{title}' not found or already borrowed."

    def returnBook(self, title):
        for book in self.books:
            if book.title == title and book.status == "borrowed":
                book.status = "available"
                return f"'{title}' has been returned."
        return f"Book '{title}' was not marked as borrowed."

    def listAvailable(self):
        available = [b.title for b in self.books if b.status == "available"]
        return available

# 17. Order & Product system – Product / Order
class ProductItem:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order:
    def __init__(self):
        self.items = [] # Stores (ProductItem, quantity)
        self.discountPercent = 0

    def addProduct(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.items.append((product, quantity))
            return True
        return False

    def applyDiscount(self, percent):
        self.discountPercent = percent

    def getTotal(self):
        subtotal = sum(p.price * q for p, q in self.items)
        discountAmount = subtotal * (self.discountPercent / 100)
        return subtotal - discountAmount

# 18. Movie Rental System – Movie / Rental
class Movie:
    def __init__(self, title, director, rentalPrice):
        self.title = title
        self.director = director
        self.rentalPrice = rentalPrice
        self.isRented = False

class Rental:
    def __init__(self):
        self.movies = []
        self.totalIncome = 0

    def rentMovie(self, title):
        for movie in self.movies:
            if movie.title == title and not movie.isRented:
                movie.isRented = True
                self.totalIncome += movie.rentalPrice
                return f"'{title}' rented successfully."
        return f"Movie '{title}' not available for rent."

    def returnMovie(self, title):
        for movie in self.movies:
            if movie.title == title and movie.isRented:
                movie.isRented = False
                return f"'{title}' returned."
        return f"Movie '{title}' was not rented out."

    def getRentedMovies(self):
        return [m.title for m in self.movies if m.isRented]

# 19. Task Manager – Task / TaskManager
class Task:
    def __init__(self, description, priority, status="Pending"):
        self.description = description
        self.priority = priority
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, description, priority):
        newTask = Task(description, priority)
        self.tasks.append(newTask)

    def markCompleted(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "Done"
                return True
        return False

    def changePriority(self, description, newPriority):
        for task in self.tasks:
            if task.description == description:
                task.priority = newPriority
                return True
        return False

    def listTasks(self):
        return [(t.description, t.priority, t.status) for t in self.tasks]

# 20. ATM Machine Simulation
class Account:
    def __init__(self, accountNumber, owner, pin, balance=1000):
        self.accountNumber = accountNumber
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.transactions = []

class Transaction:
    def __init__(self, type, amount, date):
        self.type = type # 'Deposit' or 'Withdrawal'
        self.amount = amount
        self.date = date

class ATM:
    def __init__(self):
        self.currentAccount = None

    def insertCard(self, account):
        self.currentAccount = account
        print("Card inserted.")

    def enterPin(self, pin):
        if self.currentAccount and self.currentAccount.pin == pin:
            print("PIN accepted. Welcome.")
            return True
        print("Invalid PIN.")
        return False

    def deposit(self, amount):
        if self.currentAccount and amount > 0:
            self.currentAccount.balance += amount
            log = Transaction('Deposit', amount, datetime.now())
            self.currentAccount.transactions.append(log)
            print(f"Deposited ${amount:.2f}.")
            return True
        return False

    def withdraw(self, amount):
        if self.currentAccount and 0 < amount <= self.currentAccount.balance:
            self.currentAccount.balance -= amount
            log = Transaction('Withdrawal', amount, datetime.now())
            self.currentAccount.transactions.append(log)
            print(f"Withdrew ${amount:.2f}.")
            return True
        print("Withdrawal failed (Insufficient funds or invalid amount).")
        return False

    def printStatement(self):
        if not self.currentAccount:
            print("No card inserted.")
            return
        print(f"\n--- Statement for {self.currentAccount.owner} (Account: {self.currentAccount.accountNumber}) ---")
        print(f"Current Balance: ${self.currentAccount.balance:.2f}")
        print("Transaction History:")
        for t in self.currentAccount.transactions:
            print(f"  [{t.date.strftime('%Y-%m-%d %H:%M')}] {t.type}: ${t.amount:.2f}")
        print("-------------------------------------------------------")


# --- CHẠY THỬ NGHIỆM CÁC LỚP ---

print("--- 1. Car Test ---")
c1 = Car("Tesla", "Model 3", 2023)
print(c1.getInfo())

print("\n--- 2. BankAccount Test ---")
acc = BankAccount("12345", "Alice", 100)
acc.deposit(500)
acc.withdraw(50)
print(f"Alice's final balance: ${acc.getBalance()}")

print("\n--- 3. Student Test ---")
s1 = Student("Bob")
s1.setGrade(95)
print(f"{s1.name}'s grade: {s1.getGrade()}")
try:
    s1.setGrade(105)
except ValueError as e:
    print(f"Error setting grade: {e}")

print("\n--- 4. Inheritance Test ---")
b1 = Bus(maxSpeed=100, mileage=50000, passengers=40)
print(f"Bus Max Speed: {b1.maxSpeed}, Passengers: {b1.passengers}")

print("\n--- 5. Class Method Test ---")
r1 = Robot("R2D2")
r2 = Robot("C3PO")
Robot.numberActive()
r1.remove()
Robot.numberActive()

print("\n--- 6. Polymorphism Test ---")
shapes = [Circle(5), Rectangle(4, 6)]
totalArea = sum(s.area() for s in shapes)
print(f"Total Area: {totalArea:.2f}")

print("\n--- 7. Str Test ---")
p1 = Person("Charlie", 30)
print(p1)

print("\n--- 8. Operator Overloading Test ---")
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")

print("\n--- 9. Composition Test ---")
salaryObj = Salary(pay=60000, bonus=5000)
e1 = Employee("David", salaryObj)
print(f"{e1.name}'s total compensation: ${e1.totalCompensation()}")

print("\n--- 10. Multiple Inheritance Test ---")
lfw = LogFileWriter()
lfw.processLog("System initializing")

print("\n--- 11. Singleton Test ---")
db1 = DatabaseConnection("ProdDB")
db2 = DatabaseConnection("TestDB") # Should fail to re-init
print(f"DB1 Name: {db1.dbName}, DB2 Name: {db2.dbName}")
print(f"Are instances the same? {db1 is db2}")

print("\n--- 12. Abstract Class Test ---")
d1 = Dog()
print(f"Dog says: {d1.speak()}")

print("\n--- 13. Multilevel Inheritance Test ---")
exec1 = Executive("Eve", 150000, "Sales", 50000)
print(f"Executive: {exec1.name}, Dept: {exec1.department}, Stock: {exec1.stockOptions}")

print("\n--- 14. Mixin Test ---")
prod1 = Product("Laptop", 1200.50, 10)
print(prod1.toJson())

print("\n--- 15. Property Decorator Test ---")
c_test = Circle(10)
print(f"Initial Area: {c_test.area():.2f}")
c_test.radius = 5 # Uses setter for validation
print(f"New Area: {c_test.area():.2f}")

print("\n--- 16. Library System Test ---")
lib = Library()
b_a = Book("The Great Novel", "Author X")
b_b = Book("Python Basics", "Author Y")
lib.addBook(b_a)
lib.addBook(b_b)
lib.borrowBook("The Great Novel")
print(f"Available books after borrow: {lib.listAvailable()}")
lib.returnBook("The Great Novel")
print(f"Available books after return: {lib.listAvailable()}")

print("\n--- 17. Order System Test ---")
p_apple = ProductItem("Apple", 1.5, 100)
p_banana = ProductItem("Banana", 0.5, 200)
order = Order()
order.addProduct(p_apple, 10)
order.addProduct(p_banana, 50)
order.applyDiscount(10)
print(f"Final Total: ${order.getTotal():.2f}")

print("\n--- 18. Rental System Test ---")
m1 = Movie("Inception", "Nolan", 5.00)
m2 = Movie("Tenet", "Nolan", 5.00)
rental = Rental()
rental.movies.extend([m1, m2])
rental.rentMovie("Inception")
print(f"Rented movies: {rental.getRentedMovies()}")
print(f"Total Income: ${rental.totalIncome:.2f}")

print("\n--- 19. Task Manager Test ---")
tm = TaskManager()
tm.addTask("Write report", "High")
tm.addTask("Email client", "Low")
tm.markCompleted("Write report")
tm.changePriority("Email client", "Medium")
print(tm.listTasks())

print("\n--- 20. ATM Simulation Test ---")
acc_atm = Account("998877", "John Doe", 1234)
atm = ATM()
atm.insertCard(acc_atm)
if atm.enterPin(1234):
    atm.deposit(200)
    atm.withdraw(50.50)
atm.printStatement()