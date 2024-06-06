import datetime
import re

def validate_date(date_str):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return re.match(pattern, date_str)

def calculate_days_lived(year, month, day):
    birth_date = datetime.date(year, month, day)
    current_date = datetime.date.today()
    delta = current_date - birth_date
    return delta.days

birth_date_str = input("Introduceți data nașterii (YYYY-MM-DD): ")

if validate_date(birth_date_str):
    year_of_birth, month_of_birth, day_of_birth = map(int, birth_date_str.split('-'))
    days_lived = calculate_days_lived(year_of_birth, month_of_birth, day_of_birth)
    print(f"Ați trăit {days_lived} zile până în prezent.")
else:
    print("Formatul datei introdus nu este corect.")
