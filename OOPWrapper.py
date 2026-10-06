
class Person:
    def __init__(self, name="", age=0):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        self.__age = age

    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

    def __del__(self):
        print("Person object destroyed.")


class Employee:
    def __init__(self, employee_id="", name="", age=0, salary=0):
        self.__employee_id = employee_id
        self.__name = name
        self.__age = age
        self.__salary = salary

    # Getter and Setter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter and Setter for Name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for Age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # Getter and Setter for Salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    # Display employee information
    def display(self):
        print("\nEmployee Details")
        print("-------------------------")
        print("Name       :", self.__name)
        print("Age        :", self.__age)
        print("Employee ID:", self.__employee_id)
        print("Salary     :", self.__salary)

    # Destructor
    def __del__(self):
        print("Employee object destroyed.")


# -------------------- MANAGER CLASS --------------------

class Manager(Employee):

    def __init__(
        self,
        employee_id="",
        name="",
        age=0,
        salary=0,
        department=""
    ):
        super().__init__(employee_id, name, age, salary)
        self.__department = department

    # Getter for department
    def get_department(self):
        return self.__department

    # Setter for department
    def set_department(self, department):
        self.__department = department

    # Method overriding
    def display(self):
        print("\nManager Details")
        print("-------------------------")
        print("Name       :", self.get_name())
        print("Age        :", self.get_age())
        print("Employee ID:", self.get_employee_id())
        print("Salary     :", self.get_salary())
        print("Department :", self.__department)

    # Destructor
    def __del__(self):
        print("Manager object destroyed.")


class Developer(Employee):

    def __init__(
        self,
        employee_id="",
        name="",
        age=0,
        salary=0,
        programming_language=""
    ):
        super().__init__(employee_id, name, age, salary)
        self.__programming_language = programming_language

    # Getter for programming language
    def get_programming_language(self):
        return self.__programming_language

    # Setter for programming language
    def set_programming_language(self, programming_language):
        self.__programming_language = programming_language

    # Method overriding
    def display(self):
        print("\nDeveloper Details")
        print("-------------------------")
        print("Name               :", self.get_name())
        print("Age                :", self.get_age())
        print("Employee ID        :", self.get_employee_id())
        print("Salary             :", self.get_salary())
        print("Programming Language:", self.__programming_language)

    # Destructor
    def __del__(self):
        print("Developer object destroyed.")


# -------------------- CREATE PERSON --------------------

def create_person():
    print("\n--- Create a Person ---")

    name = input("Enter Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    person = Person(name, age)

    print("\nPerson created successfully!")
    person.display()

    return person


def create_employee():
    print("\n--- Create an Employee ---")

    name = input("Enter Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    employee_id = input("Enter Employee ID: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid salary.")

    employee = Employee(
        employee_id,
        name,
        age,
        salary
    )

    print("\nEmployee created successfully!")
    employee.display()

    return employee


def create_manager():
    print("\n--- Create a Manager ---")

    name = input("Enter Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    employee_id = input("Enter Employee ID: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid salary.")

    department = input("Enter Department: ")

    manager = Manager(
        employee_id,
        name,
        age,
        salary,
        department
    )

    print("\nManager created successfully!")
    manager.display()

    return manager


def create_developer():
    print("\n--- Create a Developer ---")

    name = input("Enter Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    employee_id = input("Enter Employee ID: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid salary.")

    programming_language = input(
        "Enter Programming Language: "
    )

    developer = Developer(
        employee_id,
        name,
        age,
        salary,
        programming_language
    )

    print("\nDeveloper created successfully!")
    developer.display()

    return developer


def show_details(person, employee, manager, developer):

   
    print("SHOW DETAILS")
    

    if (
        person is None
        and employee is None
        and manager is None
        and developer is None
    ):
        print("No records available.")
        return

    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")
    print("5. All Details")

    choice = input("Enter your choice: ")

    if choice == "1":

        if person is not None:
            person.display()
        else:
            print("No Person record found.")

    elif choice == "2":

        if employee is not None:
            employee.display()
        else:
            print("No Employee record found.")

    elif choice == "3":

        if manager is not None:
            manager.display()
        else:
            print("No Manager record found.")

    elif choice == "4":

        if developer is not None:
            developer.display()
        else:
            print("No Developer record found.")

    elif choice == "5":

        if person is not None:
            person.display()

        if employee is not None:
            employee.display()

        if manager is not None:
            manager.display()

        if developer is not None:
            developer.display()

    else:
        print("Invalid choice.")


# -------------------- OOP INFORMATION --------------------

def show_oop_information():

  
    print("OOP INFORMATION")
 

    print("\n1. Encapsulation")
    print("Private attributes are used with getters and setters.")

    print("\n2. Inheritance")
    print("Manager and Developer inherit from Employee.")

    print("\n3. Method Overriding")
    print("Manager and Developer override the display() method.")

    print("\n4. Constructor Overloading")
    print(
        "Default arguments allow objects to be created "
        "with different numbers of arguments."
    )

    print("\n5. super()")
    print("super() is used to call the Employee constructor.")

    print("\n6. issubclass()")

    print(
        "Manager is subclass of Employee:",
        issubclass(Manager, Employee)
    )

    print(
        "Developer is subclass of Employee:",
        issubclass(Developer, Employee)
    )

    print(
        "Person is subclass of Employee:",
        issubclass(Person, Employee)
    )


# -------------------- MAIN PROGRAM --------------------

def main():

    person = None
    employee = None
    manager = None
    developer = None

    print("PYTHON OOP PROJECT")
 

    while True:

        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Create a Developer")
        print("5. Show Details")
        print("6. Show OOP Concepts")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            person = create_person()

        elif choice == "2":

            employee = create_employee()

        elif choice == "3":

            manager = create_manager()

        elif choice == "4":

            developer = create_developer()

        elif choice == "5":

            show_details(
                person,
                employee,
                manager,
                developer
            )

        elif choice == "6":

            show_oop_information()

        elif choice == "7":

            print("\nExiting the system...")
            print("All resources have been released.")
            print("Goodbye!")

            break

        else:

            print("\nInvalid choice!")
            print("Please enter a number between 1 and 7.")


# -------------------- PROGRAM START --------------------

if __name__ == "__main__":
    main()