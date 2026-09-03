# Урок шестой, домашнее задание №1

a = (1, 1, 2, 5, 8, 13, 21, 34, 55, 89)

smaller = []
bigger = []

for num in a:
    if num <= 5:
        smaller.append(num)
    else:
        bigger.append(num)
print(tuple(smaller))
print(tuple(bigger))

# Урок шестой, домашнее задание №2

text = input('Введите числа, разделенные запятой и проблемой: ')

nums = text.split(", ")

list = [1, 2, 3, 4, 5, 6, 7]
for n in nums:
    list.append(int(n))

print('Список чисел:', list)
print('Список чисел:', tuple)

# Урок шестой, домашнее задание №3

numbers = (12, 11, 33, 44, 55, 44, 33, 45, 30, 14, 11, 10)
list = (2, 5, 87, 22, 33, 55, 15)

unique_list = list(set(numbers))
unique_tuple = tuple(set(numbers))

print(unique_list)
print(unique_tuple)
#не понял почему ошибку выдают

# Урок шестой, домашнее задание №4

students = {}
name = 'Maksim'
age = 20
group = 'Python-120826'
print(students)
print(name)
print(age)
print(group)

# Урок шестой, домашнее задание №5

text = input('Введите строку: ')

#не понял как делать это

