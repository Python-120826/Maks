# Урок второй, домашнее задание №1

x = 6
x+=7
print(x)
y = 4
y-=1
print(y)
z = 6
z*= 1
print(z)
# Урок второй, домашнее задание №2

num1 = 3.14
num2 = 4
#"(мне непонятно это задание)"

# Урок второй, домашнее задание №3

str1 = ' pYthOn  '
str2 = ' pYthOn  '
str3 = ' pYthOn  '
str1 = str1.lower()
str2 = str2.upper()
str3 = str3.capitalize()
print(str1)
print(str2)
print(str3)

# Урок второй, домашнее задание №4

string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'
# [START:STOP:STEP]
print(string1[::-1])
print(string2[6:15])
print(string3[::2])

# Урок второй,домашнее задание №5

show = 'show ip interface brief'

display = show.replace('show', 'display')

print(display)
# мне не понятно как решать задание 6
# Урок второй, домашнее задание №7

number = int(input('Введите число:'))
digit_count = len(str(abs(number)))
print(f"Количество цифр в числе: {digit_count}")