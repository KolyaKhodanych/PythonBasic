import sys
import math
import random

# a=9
# b=6
# c = a/b
# float_var = 83.32344
# print (type(float_var))

#concatenation

# first_name = "Mykola "
# last_name = "Khodanych"
# full_name = first_name + last_name
# print(full_name)

#string *
#
# name = "Mykola"
# print(name*3)
# print(name[-1])

# print(name[0:4])

# print(len(name))

# first_name = "Mykola"
# print(first_name.title()) Метод зробить першу літеру великою
# print(first_name.upper()) Зробить всі літери великими
# print(first_name.lower()) Зробить всі літери маленькими
#
# print("Python")
# print("\tPython") Вивести з табуляцією (за замовчуванням 4 пробіли)
# print("Python is \n great") #Перенести стрічку на новий рядок

# favorite_language = " Python "
# print(favorite_language.rstrip()) #Видаляє пробіл з правого боку
# print(favorite_language.lstrip()) #Видаляє пробіл з лівого боку
# favorite_language = favorite_language.strip() # Стрічки незмінювані, їх потрібно так перезаписувати
# print(favorite_language)

#s = "EasyBACBAC     BA"
# print(s.isalnum()) # Метод перевіряє чи є СТРІЧЦІ число
# print(s.isalpha()) # Перевіряє чи ВСІ символи в стрічці є літерами
# print(s.isdecimal()) # Перевіряє чи ВСІ символи в стрічці є цифрами
# print(s.isdigit()) # Перевіряє чи всі симаоли у стрічці є числами

# print(s.islower()) # Перевіряє чи всі ЛІТЕРИ в стрічці в нижньому регістрі
# print(s.isspace()) # Перевіряє чи ВСІ символи в стрічці є пробілами
# print(s.count('BAC', 0, len(s))) # Перевіряє скільки разів зустрічається певний набір літер в певному діапазоні
#print(s.find('BA')) # Повертає індекс літери, де ВПЕРШЕ знаходить задану підстрічку
#print(s.rfind('BA')) # Повертає індекс літери, де ВОСТАННЄ знаходить задану підстрічку
#s = s.replace('BAC', 'BCD') # Замінює всі підстрічки, які знайде на задану підстрічку

print("Enter your name")
name = input()
print(f"Your name is {name}")