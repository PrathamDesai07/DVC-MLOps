class Emp:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def print_salary(self, bonus = 0):
        print(f"Salary of {self.name} is {self.salary + bonus}")


e1 = Emp(1, "Rahul", 10000)
e1.print_salary(bonus = 1000)