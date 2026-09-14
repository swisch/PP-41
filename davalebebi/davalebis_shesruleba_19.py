# დავალება 1 — თანამშრომლების სისტემა


# მშობელი კლასი Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"სახელი: {self.name}")
        print(f"ძირითადი ხელფასი: {self.salary}")

    def calculate_salary(self):
        return self.salary


# Developer კლასი
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    # Method Overriding
    def calculate_salary(self):
        return self.salary + 500

    def show_info(self):
        super().show_info()
        print(f"პროგრამირების ენა: {self.programming_language}")


# Manager კლასი
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    # Method Overriding
    def calculate_salary(self):
        return self.salary + self.team_size * 100

    def show_info(self):
        super().show_info()
        print(f"გუნდის თანამშრომლების რაოდენობა: {self.team_size}")


# Designer კლასი
class Designer(Employee):
    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    # Method Overriding
    def calculate_salary(self):
        return self.salary + 300

    def show_info(self):
        super().show_info()
        print(f"დიზაინის ხელსაწყო: {self.design_tool}")


# --------------------------------------------------------
# მომხმარებლისგან ინფორმაციის მიღება
# --------------------------------------------------------

employees = []

# მომხმარებელი უთითებს თანამშრომლების რაოდენობას
while True:
    try:
        employee_count = int(input("შეიყვანეთ თანამშრომლების რაოდენობა: "))

        if employee_count <= 0:
            print("რიცხვი უნდა იყოს 0-ზე მეტი.")
            continue

        break

    except ValueError:
        print("შეიყვანეთ რიცხვი.")


# თანამშრომლების შეყვანა
for i in range(employee_count):

    print(f"\n--- Employee {i + 1} ---")

    # სახელის შეყვანა
    name = input("შეიყვანეთ თანამშრომლის სახელი: ").strip().title()

    # ხელფასის შეყვანა
    while True:
        try:
            salary = int(input("შეიყვანეთ ძირითადი ხელფასი: "))

            if salary <= 0:
                print("ხელფასი უნდა იყოს 0-ზე მეტი.")
                continue

            break

        except ValueError:
            print("შეიყვანეთ რიცხვი.")

    # თანამშრომლის ტიპის არჩევა
    print("\nChoose employee type:")
    print("1 - დეველოპერი")
    print("2 - მანაგერი")
    print("3 - დიზაინერი")

    while True:

        employee_type = input("Enter 1, 2 or 3: ")

        # Developer
        if employee_type == "1":

            programming_language = input(
                "შეიყვანეთ პროგრამირების ენა: "
            )

            employee = Developer(
                name,
                salary,
                programming_language
            )

            break


        # Manager
        elif employee_type == "2":

            while True:
                try:
                    team_size = int(
                        input("შეიყვანეთ გუნდის თანამშრომლების რაოდენობა: ")
                    )

                    if team_size < 0:
                        print("თანამშრომლების რაოდენობა არ უნდა იყოს უარყოფითი ან 0.")
                        continue

                    break

                except ValueError:
                    print("შეცდომა! გთხოვთ შეიყვანოთ რიცხვი.")

            employee = Manager(
                name,
                salary,
                team_size
            )

            break


        # Designer
        elif employee_type == "3":

            design_tool = input(
                "შეიყვანეთ დიზაინის ხელსაწყო: "
            )

            employee = Designer(
                name,
                salary,
                design_tool
            )

            break


        else:
            print("არჩიეთ 1, 2 ან 3. გთხოვთ სცადოთ თავიდან.")


    # შექმნილ ობიექტს ვამატებთ სიაში
    employees.append(employee)


# --------------------------------------------------------
# Polymorphism
# --------------------------------------------------------

print("\n===== თანამშრომლები =====")

for employee in employees:

    print("\n-------------------------")

    employee.show_info()

    print(
        f"სამომავლე ხელფასი: {employee.calculate_salary()}"
    )