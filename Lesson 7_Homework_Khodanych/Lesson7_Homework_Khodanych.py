# Завдання 1
def domain_lines(file):
    """
    Функція виводить стрічки, що містяться у заданому файлі, починаючи з другого символу
    """
    file_open = open(file, "r")
    for lines in file_open:
        print(lines[1:])

domain_lines("domains.txt")

# Завдання 2

def surname_extractor(file):
    """
    Функція розбиває рядок на елементи масиву і виводить другий елемент (Прізвище)
    """
    file_open = open(file, "r")
    for lines in file_open:
        line_list = lines.split(" ")
        surname = line_list[1]
        print(surname)

surname_extractor("names.txt")

# Завдання 3

def create_dict_from_file(file):
    """
    Функція створює список словників виду {'date': date}, де замість date підставляє
    перші три слова стрічки (дата)), стрічка розглядаєтсья тільки за умови, якщо в ній більше
    3 слів
    """
    with open(file) as f:
        lines = f.readlines()
        dict_list = []
        for line in lines:
            line = line.strip()
            if len(line.split()) > 3:
                date = " ".join(line.split()[:3])
                dict_list.append({"date": date})
        print(dict_list)


create_dict_from_file("authors.txt")

# Завдання 4

def sort_file_by_length(file_name):
    """
    Функція сортує рядки за довжиною від найкоротшої до найдовшої, і перезаписує файл
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()

    lines.sort(key=len)

    with open(file_name, 'w') as file:
        file.writelines(lines)

sort_file_by_length("file_for_sorted.txt")


