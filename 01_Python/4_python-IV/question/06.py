from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def  calculate_salary(self):
        pass 

class Intern(Employee):
    def __init__(self, salary):
        self.salary = salary

    def  calculate_salary(self):
        print(self.salary *12)

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def  calculate_salary(self):
        print(self.salary *12)

class ContractEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def  calculate_salary(self):
        print(self.salary *12)


I = Intern(20_000)
I.calculate_salary()                

E = FullTimeEmployee(2_00_000)
E.calculate_salary()