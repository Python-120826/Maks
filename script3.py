#Урок третий, домашнее задание №1

number1 = int(input("Введите число: "))
if number1 > 0:
    number1 += 20
else:
    number1 -=5
    print(number1)

#Урок третий, домашнее задание №2

# я не понял как решать задание 2

#Урок третий, домашнее задание №3

temperature = int(input("Введите температуру: "))
if temperature <= 37:
    print('Здоров')
else:
    print('Болен')

#Урок третий, домашнее задание №4
# Температура тания льда равна 0 градусов

temperature1 = int(input("Введите первое значение: "))
temperature2 = int(input("Введите второе значение: "))
temperature3 = int(input("Введите третье значение: "))
if temperature1 > temperature2:
    print('Температура льда')
else:
    print("Слабое градус")

#Урок третий, домашнее задание №5

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a % 2 == 0:
    print(f"{a} четное")
else:
    print(f"{a} нечетное")

if b % 2 == 0:
    print(f"{b} четное")
else:
    print(f"{b} нечетное")