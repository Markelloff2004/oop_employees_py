import math

def calculate_fall_time(height):
    g = 9.8
    time = math.sqrt(2 * height / g)
    return time

height_str = input("Introduceți înălțimea căderii (în metri): ")

try:
    height = float(height_str)
    if height < 0:
        print("Înălțimea trebuie să fie un număr pozitiv.")
    else:
        fall_time = calculate_fall_time(height)
        print(f"Timpul de cădere pentru înălțimea {height} metri este de aproximativ {fall_time:.2f} secunde.")
except ValueError:
    print("Introduceți un număr valid pentru înălțime.")
