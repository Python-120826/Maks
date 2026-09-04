# Урок седьмой, домашнее задание №1

val1 = input("Введите первое значение: ")
val2 = input("Введите первое значение: ")

try:
    result = int(val1) + int(val2)
except ValueError:
    result = val1 + val2
print(f"Результат: {result}")

# Урок седьмой, домашнее задание №2

list1 = [1, 'a',3, 'b', 5, '6', 7, '8', 9, 'c']

numbers = []
strings = []

for item in list1:
    try:
        numbers.append(item)
    except TypeError:
        strings.append(item)

print("Числа:", numbers)
print("Строки:", strings)

# Урок седьмой, домашнее задание №3

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        pass

print(fifth)

# Урок седьмой, домашнее задание №4

my_list = [2, 'C', 10, '20', 20, 'micros', 50, 0, '0', '30', 30]

for index in range(len(my_list) + 5):
    try:
        item = my_list(index)
        result = item / item
    except TypeError:
        print(f"Ошибка TypeError: '{item}' так как тип элемента {type(item)}")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except IndexError:
        print(f"Список оказался слишком мал, индекс под номером {index} не существует")
    else:
        print(f"{item} / {item} = {result}")
        print(f"Все получилось с первой попытки, так как элемент {item} является числом")


# Урок седьмой, домашнее задание №5

try:
    min_num = int(input("Введите первое число: "))
    max_num = int(input("Введите второе число: "))

    for i in range(min_num, max_num + 1):
        print(f"Квадрат числа {i} равен {i * i}")
except ValueError:
    print("Ошибка: нужно было ввести целое число!")