# position, name, age, level, salary
engineer_one = ["Software Engineer", "Max", 20, "Junior", 5000]
engineer_two = ["Software Engineer", "Lias", 25, "Senior", 7000]


# class
class SoftwareEngineers:
    # class attribute
    alias = "Code Father"

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# instance of the class SoftwareEngineer
first_engineer = SoftwareEngineers("Max", 20, "Junior", 5000)
print(first_engineer.name, first_engineer.age)
print(SoftwareEngineers.alias)
second_engineer = SoftwareEngineers("Lias", 25, "Senior", 7000)
print(second_engineer.name, second_engineer.age)
print(SoftwareEngineers.alias)
