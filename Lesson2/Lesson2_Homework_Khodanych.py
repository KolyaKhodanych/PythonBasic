import math

# Завдання 1

# 1.1 task

first_name = input("Hi!) Enter your first name ")
last_name = input("Enter your last name ")
full_name = first_name.title()+" "+last_name.title()

print(f"Nice to meet you {full_name})")

# 1.2 task

print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# 1.3 task

five_names = (full_name + " ") * 5
print(five_names)

# 1.4 task

full_name = f"  \t{first_name}  \n{last_name}  "
print(full_name)

full_name = full_name.lstrip()
full_name = full_name.rstrip()

print(full_name)

# Завдання 2


print("\nWelcome to the circle length and the area of a circle calculator!")

radius = input("Enter the radius of your circle: ")
circle_length = 2 * math.pi * float(radius)
circle_area = math.pi * pow(float(radius),2)

print(f"\nThe length of this circle is {circle_length} cm")
print(f"The area of this circle is {circle_area} сm²")

# Завдання 3

current_dollar_rate = 36.92
print("\nwelcome to currensy exchange!)")
sum = input("\nhow many dollars do you want to buy? ")
convertor = float(sum) * float(current_dollar_rate)
print(f"\nit will be {round(convertor,2)} Ukrainian hryvnias for 24.12.2022")

print("\nThanks... bye!)")