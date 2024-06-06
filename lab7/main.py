import re
from employees import Employee, HourlyEmployee, SalaryEmployee

def validate_input(prompt, pattern):
    value = input(prompt)
    while not re.match(pattern, value):
        print("Valoare invalidă. Încercați din nou.")
        value = input(prompt)
    return value

def create_salary_employee():
    name = validate_input("Introduceți numele: ", r'^[a-zA-Z]+$')
    phone = validate_input("Introduceți telefonul (+373cccccccc): ", r'^\+373\d{8}$')
    bday = validate_input("Introduceți data nașterii (dd.mm.yyyy): ", r'^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(196[0-9]|19[7-9][0-9]|200[0-7])$')
    email = validate_input("Introduceți email-ul: ", r'^[a-zA-Z0-9._-]+@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$')
    position = validate_input("Introduceți specialitatea: ", r'^[a-zA-Z]{4,20}$')
    salary = float(validate_input("Introduceți salariul lunar: ", r'^\d+(\.\d+)?$'))
    return SalaryEmployee(name, phone, bday, email, position, salary)

def create_hourly_employee():
    name = validate_input("Introduceți numele: ", r'^[a-zA-Z]+$')
    phone = validate_input("Introduceți telefonul (+373cccccccc): ", r'^\+373\d{8}$')
    bday = validate_input("Introduceți data nașterii (dd.mm.yyyy): ", r'^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(196[0-9]|19[7-9][0-9]|200[0-7])$')
    email = validate_input("Introduceți email-ul: ", r'^[a-zA-Z0-9._-]+@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$')
    position = validate_input("Introduceți specialitatea: ", r'^[a-zA-Z]{4,20}$')
    mbrOYour = int(validate_input("Introduceți numărul de ore lucrate: ", r'^\d+$'))
    hourlyPay = float(validate_input("Introduceți plata pe oră: ", r'^\d+(\.\d+)?$'))
    return HourlyEmployee(name, phone, bday, email, position, mbrOYour, hourlyPay)

def main():
    employees = []

    employees.append(create_salary_employee())
    employees.append(create_hourly_employee())

    for emp in employees:
        print(f"{emp.name}, poziția: {emp.position}, salariu: {emp.calculateSalary()}")

    with open("data.txt", "w") as file:
        for emp in employees:
            file.write(f"{emp.name},{emp.phone},{emp.bday},{emp.email},{emp.position},{emp.calculateSalary()}\n")

    print("Datele au fost salvate în fișierul data.txt.")

if __name__ == "__main__":
    main()