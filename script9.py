# Урок восьмой, домашнее задание №1

count = 0

with open('mbox-short.txt', 'r', encoding='utf8') as file:
    for line in file:

        line = line.strip()

        if line.startswith('From '):
            words = line.split()
            if len (words) > 1:
                email = words[1]
                print(email)
                count += 1

print(f"Кол-во входящих писем: {count}")

# Урок восьмой, домашнее задание №2

file = open('romeo.txt', 'r', encoding='utf-8')
unique_words = []

for line in file:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

unique_words.sort()
print(unique_words)

# Урок восьмой, домашнее задание №3

# lines = int(input('Сколько последних строк распечатать: '))
#
# if lines > 0:
#     with open('pushkin.txt', 'w', encoding='utf8') as file:
#        all_lines = file.readlines()
#
#        last_lines = all_lines[-lines:]
#
#        for line in last_lines:
#            print(line.strip())
#Не знаю зачем и почему выдает ошибку хотя все правильно показывает

# Урок восьмой, домашнее задание №4

with open('pushkin.txt', 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split()
clean_words = [word.strip('.,!?-—":;()') for word in words]

max_len = 0
longest_words = []

for word in clean_words:
    if len(word) > max_len:
        max_len = len(word)
        longest_words = [word]
    elif len(word) == max_len and word not in longest_words:
        longest_words.append(word)

print(longest_words)