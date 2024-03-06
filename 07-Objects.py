# Classes execute each line of code in them during instantiation
class Employee:
    print("Employee instance created!")

emp = Employee()

# You can pre initiate properties
class Employee:
    name = "Serdar"

emp = Employee()
print(emp.name)

# You create class methods with self as input parameter
class Employee:
    name = "Method"
    def print(self):
        print(self.name)

emp = Employee()
emp.print()
del emp

# You create an initializer using __init__ special word
class Employee:
    def __init__(self, id, name, title, department) -> None:
        self.id = id
        self.name = name
        self.title = title
        self.department = department

emp = Employee(1, "Serdar", "Engineering Manager", "Technology")

# You can implement str function for the class
class Employee:
    def __init__(self, id, name, title, department) -> None:
        self.id = id
        self.name = name
        self.title = title
        self.department = department
    def __str__(self) -> str:
        return str(self.id) + ": " + self.name + ", " + self.title + ", " + self.department

emp = Employee(1, "Serdar", "Engineering Manager", "Technology")
print(str(emp))
del emp
# Methods to update properties
class Employee:
    def __init__(self, id, name, title, department, salary) -> None:
        self.id = id
        self.name = name
        self.title = title
        self.department = department
        self.salary = salary
    def __str__(self) -> str:
        return str(self.id) + ": " + self.name + ", " + self.title + ", " + self.department + ", salary: " + str(round(self.salary, 2))
    def makeRaise(self, percentage):
        self.salary = self.salary + self.salary * percentage

emp = Employee(1, "Serdar", "Engineering Manager", "Technology", 105000)
emp.makeRaise(0.08)
print(str(emp))
del emp
# Static Methods
class Employee:
    def __init__(self, id, name, title, department, salary) -> None:
        self.id = id
        self.name = name
        self.title = title
        self.department = department
        self.salary = salary
    def __str__(self) -> str:
        return str(self.id) + ": " + self.name + ", " + self.title + ", " + self.department + ", salary: " + str(round(self.salary, 2))
    def makeRaise(self, percentage):
        self.salary = self.salary + self.salary * percentage
    def year(): # Static
        return 2024

print(Employee.year())

# Inheritence
class Manager(Employee):
    def __init__(self, id, name, title, department, salary, reports) -> None:
        super().__init__(id, name, title, department, salary)
        self.reports = reports
    def __str__(self) -> str:
        return super().__str__() + ", team size: " + str(self.reports)
person = Manager(1, "Serdar", "Engineering Manager", "Technology", 105000, 20)

person.makeRaise(0.05)
print(str(person))
