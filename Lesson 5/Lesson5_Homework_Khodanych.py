# Спосіб 1
notes = []

while True:
    command = input("Введіть команду: (add, earliest, latest, longest, shortest, exit): ")

    def add_note():
        """
        Функція додає елементи (нотатки) у масив notes
        """
        note = input("Введіть текст нотатки: ")
        notes.append(note)

    def earliest_note():
        """
        Функція виводить елементи notes від найновішого елемента до найстарішого
        """
        for note in notes:
            print(note)

    def latest_note():
        """
        Функція виводить елементи notes від найстарішого елемента до найновішого
        """
        for note in reversed(notes):
            print(note)

    def longest_note():
        """
        Функція виводить елементи notes від найдовшого елемента до найкоротшого
        """
        notes.sort(key=len, reverse=True)
        for note in notes:
            print(note)

    def shortest_note():
        """
        Функція виводить елементи notes від найдовшого елемента до найкоротшого
        """
        notes.sort(key=len)
        for note in notes:
            print(note)


    if command == "add":
        add_note()
    elif command == "earliest":
        earliest_note()
    elif command == "latest":
        latest_note()
    elif command == "longest":
        longest_note()
    elif command == "shortest":
        shortest_note()
    elif command == "exit":
        break
    else:
        print("Такої команди не існує(")


# # Спосіб 2
#
# notes = []
#
# while True:
#     command = input("Введіть команду: (add, earliest, latest, longest, shortest, exit): ")
#
#     if command == "add":
#         text = input("Введіть текст нотатки: ")
#         notes.append(text)
#     elif command == "earliest":
#         print("Виводжу нотатки від найновішої до найстарішої:")
#         for note in reversed(notes):
#             print(note)
#     elif command == "latest":
#         print("Виводжу нотатки від найстарішої до найновішої:")
#         for note in notes:
#             print(note)
#     elif command == "longest":
#         print("Виводжу нотатки від найдовшої до найкоротшої:")
#         notes.sort(key=len, reverse=True)
#         for note in notes:
#             print(note)
#     elif command == "shortest":
#         print("Виводжу нотатки від найкоротшої до найдовшої:")
#         notes.sort(key=len)
#         for note in notes:
#             print(note)
#     elif command == "exit":
#         print("Буду радий бачити знову)")
#         break
#     else:
#         print("Такої команди не передбачено")
