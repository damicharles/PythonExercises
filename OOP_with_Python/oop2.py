# position, name, age, level, salary
first_engineer = ["Software Engineer", "Max", 20, "Junior", 5000]
second_engineer = ["Software Engineer", "Lias", 25, "Senior", 7000]
d1 = ["Designer", "Phillip"]


# class
class SoftwareEngineer:
    # class attribute
    alias = "Code Father"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code.....")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}....")

    # def information(self):
    #   information = f"name = {self.name}, age = {self.age}, level = {self.level}"
    #  return information

    # dunder methods
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


# instance of the class SoftwareEngineer
first_engineer = SoftwareEngineer("Max", 20, "Junior", 5000)
second_engineer = SoftwareEngineer("Lias", 25, "Senior", 7000)
se3 = SoftwareEngineer("Liass", 25, "Senior", 7000)

first_engineer.code()
second_engineer.code()
first_engineer.code_in_language("Python")
second_engineer.code_in_language("Java")
# print(se1.information())
# print(se2 == se3)
# print(se2)
# in line 60 works because of the static method indicated on line 38
print(first_engineer.entry_salary(24))
print(SoftwareEngineer.entry_salary(27))
