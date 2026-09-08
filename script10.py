#Урок девятый, домашнее задание №1
from operator import truediv


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#Урок девятый, домашнее задание №2

def custom_filter(data, **kwargs):
    result = []
    for item in data:
        match = True
        for key, value in kwargs.items():
            if item.get(key) != value:
                match = False
                break
        if match:
            result.append(item)
    return result

#Урок девятый, домашнее задание №3

def advanced_logger(*args, **kwargs):
    uppercase = kwargs.get('uppercase', False)
    prefix = kwargs.get('prefix', '')

    for message in args:
        text = str(message)
        if uppercase:
            text = text.upper()
        if prefix:
            text = f"{prefix} {text}"
# print(text)
#Не знаю почему выдает ошибку

#Урок девятый, домашнее задание №4

#Не понял как это делать

#Урок девятый, домашнее задание №7

names = ["Behzod", "Sergey", "Andrey", "Akmal"]
grades = [90, 70, 88, 84]

result7 = [name for name, grade in zip(names, grades) if grade >= 85]
print(result7)

#Урок девятый, домашнее задание №8

products = ["яблоко", "банан", "вишня", "груша"]
quantities = [1, 3, 2, 5]

result8 = [prod.upper() for prod,qty in zip(products, quantities) if qty >= 2]
print(result8)

#Урок девятый, домашнее задание №9

names = ["Behzod", "Sergey", "Andrey", "Akmal"]
grades = [
    [90, 88, 92],
    [70, 72, 68],
    [85, 86, 90],
    [80, 82, 81]
]

result9 = [
    name for name, grade in zip(names, grades)
    # if (sum(student_grades) / len(student_grades)) > 85
]
print(result9)

#Почемуто выдовало ошибку

#Урок девятый, домашнее задание №10

names = ["Behzod", "Sergey", "Andrey", "Akmal"]
positions = ["менеджер", "инженер", "менеджер", "аналитик"]
salaries = [70000, 80000, 55000, 60000]

result10 = [
    name for name, pos, salary in zip(names, positions, salaries)
    if pos == "Менеджер" and salary >= 60000
]
print(result10)