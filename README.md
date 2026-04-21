Employee Management System (Python OOP Project)
📌 Overview
This project is a simple Employee Management System built using Object-Oriented Programming (OOP) concepts in Python.
It demonstrates key OOP principles such as encapsulation, inheritance, polymorphism, and method overriding.

🚀 Features
Create different types of records:
👤 Person
🧑‍💼 Employee
🧑‍💼 Manager
👨‍💻 Developer
Display details based on selected category
Encapsulation using private attributes (__employee_id, __salary)
Inheritance for specialized roles (Manager, Developer)
Method overriding (display() method)
Menu-driven interactive program

🏗️ Class Structure
🔹 Person
Attributes: name, age
Method:
display()
🔹 Employee (Base Class)
Attributes:
employee_id (private)
name
age
salary (private)
Methods:
Getters & Setters:
get_employee_id(), set_employee_id()
get_salary(), set_salary()
display()
__del__() (destructor)
🔹 Manager (Derived Class)
Inherits from Employee
Additional Attribute:
department
Overrides:
display()
🔹 Developer (Derived Class)
Inherits from Employee
Additional Attribute:
programming_language
Overrides:
display()

📋 Menu Options
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Exit

💡 Concepts Used
✅ Classes & Objects
✅ Constructors (__init__)
✅ Destructors (__del__)
✅ Encapsulation (private variables)
✅ Inheritance
✅ Method Overriding
✅ Polymorphism (display() method)
✅ List for data storage
✅ isinstance() for type checking

⚠️ Notes
The destructor (__del__) is used for demonstration; in Python it is not guaranteed to execute immediately.
Employee ID and Salary are private attributes and should be accessed using getters/setters.
📈 Future Improvements
🔍 Search employee by ID
✏️ Update employee details
❌ Delete employee records
💾 Save data to file (JSON/CSV)
🖥️ Add GUI (Tkinter / PyQt)

👨‍💻 Author
Bhumi Shah
