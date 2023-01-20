from collections import Counter

# Завдання 1

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_numbers = sorted(set(list1) & set(list2))
print(f"Спільні елементи - {common_numbers}")

# Завдання 2

student_dict = {'Микита Клочко': 700, 'Олександр Осадчий': 672, 'Володимир Коломацький': 647,
                'Микола Ходанич': 591, 'Святослав Николин': 505}

average = sum(student_dict.values()) / len(student_dict)
print(f"\nСередній бал групи: {average}")
print("Студенти з балом вище середнього:")
for key, value in student_dict.items():
    if value > average:
        print(key)

# Завдання 3

numbers = [1, 2, 3, 2, 3, 4, 5, 6, 7, 5, 8, 9, 8, 9, 10]
unique_numbers = set(numbers)
count = len(unique_numbers)
print(f"\nКількість різних значень у цьому списку: {count}")

# Завдання 4

list1 = [int(i) for i in input("\nВведіть перший список: ").split()]  # вводимо список у вигляді 1 2 3
list2 = [int(i) for i in input("Введіть другий список: ").split()]

result = list(set(list1) & set(list2))
result.sort()

print("Числа, які присутні в обох списках в порядку зростання:")
print(*result)

# Завдання 5

text = "one two three one four five seven ten seven one"
words = text.split()
word_counts = Counter(words)
print("")
for word, count in word_counts.items():
    print("({}, {})".format(word, count))
