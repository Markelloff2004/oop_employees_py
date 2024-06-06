import calendar

from sarcina6_1 import validate_date


def get_weekday_text(year, month, day):
    days = ["Luni", "Marți", "Miercuri", "Joi", "Vineri", "Sâmbătă", "Duminică"]
    weekday_number = calendar.weekday(year, month, day)
    return days[weekday_number]

date_str = input("Introduceți data (YYYY-MM-DD): ")

if validate_date(date_str):
    year, month, day = map(int, date_str.split('-'))
    weekday_text = get_weekday_text(year, month, day)
    print(f"Data {date_str} este o zi de {weekday_text}.")
else:
    print("Formatul datei introdus nu este corect.")
