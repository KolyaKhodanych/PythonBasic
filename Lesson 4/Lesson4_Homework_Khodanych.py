# Завдання 1

given_number = float(input("Введіть число для перевірки: "))

def in_range (to, since = 0) -> bool: #Не дозволяє назвати параметр "from"
    """
    Checking if the given number is in a range
    """
    return given_number >= since and given_number <= to


print(in_range(12, -20))

# Завдання 2

def arithmetic(a: int, b: int, operation: str):
    """
    function to perform simple arithmetic operations
    """
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        print(a/b)
    elif operation == "**":
        print(a**b)
    elif operation == "%":
        print(a%b)
    elif operation == "//":
        print(a//b)
    else:
        print("Операція неможлива")

arithmetic(a = 9,b = 9, operation = "**")

# Завдання 3

quote = input("Введіть цитату для перевірки на паліндром: ")


def is_palindrome(quote: str):
    """
    The function checks whether a phrase is a palindrome
    """
    reversed_quote = ''.join(reversed(quote))
    if quote == reversed_quote:
        print("Так, фраза - паліндром)")
    else:
        print("Це не паліндром(")


is_palindrome(quote)

# Завдання 4

some_string = input("Введіть стрічку: ")
args = ["S", "o"] #Тут вводяться символи, які слід видалити

def sicario(some_string, args=''):
    """the function removes the selected characters from the string"""
    new_string = some_string.translate(str.maketrans('', '', ''.join(args)))
    print(new_string)

sicario(some_string, args)
