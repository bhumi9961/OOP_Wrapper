print("--- Python OOP Project: Employee Management System ---")

employees = []

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Person created with name: {self.name} and age: {self.age}")
    
class Employee: 
    def __init__(self, employee_id, name, age, salary):
        self.__employee_id = employee_id
        self.name = name
        self.age = age
        self.__salary = salary
    
    #setter for employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    
    #getter for employee ID
    def get_employee_id(self):
        return self.__employee_id
    
    #setter for salary
    def set_salary(self, salary): 
        self.__salary = salary
    
    #getter for salary
    def get_salary(self): 
        return self.__salary
    
    def __del__(self):
        print(f"Data of employee with name: {self.name}, Employee_id: {self.__employee_id}, Age : {self.age} and Salary : {self.__salary} is destroyed")
    
    def display(self):
        print("Employee_ID: ", self.__employee_id)
        print("Name: ", self.name)
        print("Age: ",self.age)
        print("Salary: ", self.__salary)


class Manager(Employee):
    def __init__(self, employee_id, name, age, salary, department):
        super().__init__(employee_id, name, age, salary)
        self.department = department
    
    def display(self):
        super().display()
        print("Department: ",self.department)

class Developer(Employee):
    def __init__(self, employee_id, name, age, salary, programming_language):
        super().__init__(employee_id, name, age, salary)
        self.programming_language = programming_language
    
    def display(self):
        super().display()
        print("Programming Language: ",self.programming_language)

        

while True:
    print("\n Choose an operation: \n" \
    "1. Create a Person \n" \
    "2. Create an Employee \n" \
    "3. Create a Manager \n" \
    "4. Create a Developer \n" \
    "5. Show Details \n" \
    "6. Exit")

    choice = int(input("Please Enter Your Choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        age = int(input("Enter your age: "))
        person = Person(name, age)
        employees.append(person)
        
    elif choice == 2:
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter employee salary: $"))
        employee = Employee(employee_id, name, age, salary)
        employees.append(employee)
        print(issubclass(Employee,object))
    
    elif choice == 3: 
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter employee salary: $"))
        department = input("Enter Department: ")
        manager = Manager(employee_id, name, age, salary, department)
        employees.append(manager)
        print(issubclass(Manager, Employee))

    elif choice == 4: 
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter employee salary: $"))
        programming_language = input("Enter Programming Language: ")
        developer = Developer(employee_id, name, age, salary, programming_language)
        employees.append(developer)
        print(issubclass(Manager, Employee))

    elif choice == 5:
        print("Choose details to show: \n" \
        "1. Person \n" \
        "2. Employee \n" \
        "3. Manager \n" \
        "4. Developer")

        choosen = int(input("Enter your choice: "))
        for emp in employees:
            if choosen == 1 and isinstance(emp, Person):
                print("\n-----Person-----")
                emp.display()
                found = True
            
            elif choosen == 2 and isinstance(emp, Employee) and not isinstance(emp, (Manager, Developer)):
                print("\n-----Employee-----")
                emp.display()
                found = True
                
            elif choosen == 3 and isinstance(emp, Manager):
                print("\n-----Manager-----")
                emp.display()
                found = True
            
            elif choosen == 4 and isinstance(emp, Developer):
                print("\n-----Developer-----")
                emp.display()
                found = True

        if not found: 
            print("Invalid Choice!!!!")
    
    elif choice == 6:
        print("Exiting the program...")
        break

    else:
        print("Invalid Choice!!!")