# Composite Design Pattern
# Increase flexibility and makes
# structure easier to use

# Multiple classes that inherit from the same
# interface or parent class and one can consist of
# many of the others.


# We will have a parent department with many subdepartments

from abc import ABCMeta, abstractstaticmethod

# Department Interface
class IDepartment(metaclass=ABCMeta):

    # Abstract constructor (method)
    @abstractstaticmethod
    def __init__(self, employees):
        """ implement in child class """


    @abstractstaticmethod
    def print_department():
        """ implement in child class """

#Concrete class that inherit from abstract base class (interface)
class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")


#Concrete class that inherit from abstract base class (interface)
class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")

# Parent Dept that adds the two departments together
class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        # how many in parent without being in child department
        self.base_employees = employees
        self.sub_depts = []

    # add method that appends department to list
    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    # Prints the departments
    def print_department(self):
        print("Parent Department")
        print(f"Parent Department Base employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of number of employees: {self.employees}")

dept1 = Accounting(220)
dept2 = Development(120)

parent_dept = ParentDepartment(30)
# dept1,2 are passed to add function and adds to department total
parent_dept.add(dept1)
parent_dept.add(dept2)

# prints the total number after being added
parent_dept.print_department()
