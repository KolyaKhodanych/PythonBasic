# Задача 1
import random

min = random.randint(0, 59)
print(f"Рандомне число: {min}")

if min >= 0 and min <= 15:
    print ("Це число потрапляє у першу чверть")
elif min >= 15 and min <= 30:
    print("Це число потрапляє у другу чверть")
elif min >= 30 and min <= 45:
    print("Це число потрапляє у третю чверть")
elif min >= 45 and min <= 60:
    print("Це число потрапляє у четверту чверть")

# Задача 2

birth_month = int(input("Введіть місяць вашого народження: "))

if birth_month < 1 or birth_month > 12:
    print("Введіть число від 1 до 12 (Адже стільки місяців))")
elif birth_month == 12 or birth_month == 1 or birth_month == 2:
    print("Зима - За вікном падав сніг.")
elif birth_month == 3 or birth_month == 4 or birth_month == 5:
    print("Весна - Все довкола розцвітало.")
elif birth_month == 6 or birth_month == 7 or birth_month == 8:
    print("Літо - Діти насолоджувались літніми канікулами.")
else:
    print("Осінь - Все довкола загоралось яскравими фарбами.")

# Задача 3


number = random.randint(1, 10000)
print(f"Рандомне число: {number}")
sum_of_digits = sum(map(int, list(str(number))))
print(f"Сума цифр числа: {sum_of_digits}")
last_digit = number % 10

if last_digit % 2 == 0 and sum_of_digits % 3 == 0:
    print("Це число ділиться на 6")
else:
    print("Це число не ділиться на 6")

# Задача 4

x_point = float(input("Введіть координату Х: "))
y_point = float(input("Введіть координату Y: "))

if x_point > 0 and y_point > 0:
    print("Точка знаходиться у першій чверті")
elif x_point < 0 and y_point > 0:
    print("Точка знаходиться у другій чверті")
elif x_point < 0 and y_point < 0:
    print("Точка знаходиться у третій чверті")
elif x_point > 0 and y_point < 0:
    print("Точка знаходиться у четвертій чверті")
else:
    print("Це початок координат)")
