# inherit, extend, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")

    def debug(self):
        print(f"{self.name} is debugging...")


class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")
    # pass


se = SoftwareEngineer("Max", 25, 6000, "Junior")
# print(se.name, se.age)
se.work()
# print(se.level)
# (se.debug())

d = Designer("Philip", 27, 7000)
# print(d.name, d.age)
d.work()
# (d.draw())


# Polymorphism

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Philip", 27, 7000)]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employees)

# Recap
# Inheritance: ChildClass(BaseClass)
# Inherit, extend and override attributes and functions
# Super()__init__()
# Polymorphism
