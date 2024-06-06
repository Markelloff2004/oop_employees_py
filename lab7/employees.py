import datetime
import re

class Employee:
    def __init__(self, name, phone, bday, email, position):
        self._name = name
        self._phone = phone
        self._bday = bday
        self._email = email
        self._position = position

    def calculateAge(self):
        today = datetime.date.today()
        bday = datetime.datetime.strptime(self._bday, "%d.%m.%Y").date()
        age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
        return age

    def calculateSalary(self):
        pass  # Va fi rescris de clasele mostenitoare

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r'^[a-zA-Z]+$', value):
            self._name = value
        else:
            raise ValueError("Numele trebuie să conțină doar litere.")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if re.match(r'^\+373\d{8}$', value):
            self._phone = value
        else:
            raise ValueError("Telefonul trebuie să corespundă șablonului +373cccccccc.")

    @property
    def bday(self):
        return self._bday

    @bday.setter
    def bday(self, value):
        if re.match(r'^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(196[0-9]|19[7-9][0-9]|200[0-7])$', value):
            self._bday = value
        else:
            raise ValueError("Data nașterii trebuie să corespundă șablonului dd.mm.yyyy și să fie între 1960 și 2007.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z]{4,7}\.[a-zA-Z]{2,4}$', value):
            self._email = value
        else:
            raise ValueError("Email-ul trebuie să corespundă unui format valid.")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if re.match(r'^[a-zA-Z]{4,20}$', value):
            self._position = value
        else:
            raise ValueError("Specialitatea trebuie să conțină doar litere, între 4 și 20.")


class HourlyEmployee(Employee):
    def __init__(self, name, phone, bday, email, position, mbrOYour, hourlyPay):
        super().__init__(name, phone, bday, email, position)
        self._mbrOYour = mbrOYour
        self._hourlyPay = hourlyPay

    @property
    def mbrOYour(self):
        return self._mbrOYour

    @mbrOYour.setter
    def mbrOYour(self, value):
        if value >= 0:
            self._mbrOYour = value
        else:
            raise ValueError("Numărul de ore lucrate trebuie să fie un număr pozitiv.")

    @property
    def hourlyPay(self):
        return self._hourlyPay

    @hourlyPay.setter
    def hourlyPay(self, value):
        if value >= 0:
            self._hourlyPay = value
        else:
            raise ValueError("Plata pe oră trebuie să fie un număr pozitiv.")

    def calculateSalary(self):
        return self._mbrOYour * self._hourlyPay


class SalaryEmployee(Employee):
    def __init__(self, name, phone, bday, email, position, salary):
        super().__init__(name, phone, bday, email, position)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salariul trebuie să fie un număr pozitiv.")

    def calculateSalary(self):
        return self._salary
