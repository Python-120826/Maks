#Урок 4, домашнее задание №1
# from datetime import datetime
#
# name = input('Введите свое имя: ')
# birth_year = input('Введите свой год рождения: ')
# current_year = datetime.now()
# age = current_year - birth_year
# print(f'{name}, ваш возраст:{age}')
#почему то тут ошибку выдают

#Урок 4, домашнее задание №2

month = int(input('Введите номер месяца: '))

match month:
    case 1: print('Январь')
    case 2: print('Февраль')
    case 3: print('Март')
    case 4: print('Апрель')
    case 5: print('Май')
    case 6: print('Июнь')
    case 7: print('Июль')
    case 7: print('Август')
    case 8: print('Сентябрь')
    case 9: print('Октябрь')
    case 10: print('Ноябрь')
    case 11: print('Декабрь')
    case _: print('Неверный месяц')

#Урок 4, домашнее задание N3

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
if x == y == z:
    count = 3
if x == y or y == z or x == z:
    count = 2
else:
    count = 0

print(f"Количество совпадающих чисел: {count}")

#Урок 4, домашнее задание №4(не понял я как это решать)

#Урок 4, домашнее задание №5(Условие понятно а само задание мне нет)

# width = int(input('Введите ширину: '))
# length = int(input('Введите длину: '))
# parts = int(input('Введите количество долек: '))

#Урок 4, домашнее задание №6(тоже не понял)

#Урок 4, домашнее задание №7(эти 4 задания я не понимаю как делать)

#Урок 4, домашнее задание №8

seconds = int(input("Введите количество секунд: "))

for i in range(seconds, 0, -1):
    print(f"Осталось секунд: {i}")
print("Старт!")

#Урок 4, домашнее задание №9(ничего не понял как)

#Урок 4, домашнее задание №10(Не понял)

