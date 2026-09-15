#Урок десятый,дз №1

#чуть чуть не понял здесь

#Урок десятый,дз №2

import re

sample = 'exercises numbers 1, 12, 13, and 345 are important 456'

result = re.findall(r'\b\d{3}\b', sample)
print(result)

#Урок десятый,дз №3

import re

colors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000']
pattern = r'^#[0-9A-Fa-f]{6}$'

valid_colors = [c for c in colors if re.match(pattern, c)]
print(valid_colors)

#Урок десятый,дз №4

import re

text = ['Завтрак в 09:00', 'Завтрак в 90:00', 'Обед в 13:00', 'Обед в 13:61', 'Ужин в 19:05', 'Ужин в 37:98', 'Ужин в 24:01']
pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d\b'

valid_text = [t for t in text if re.search(pattern, t)]

print(valid_text)

#Урок десятый,дз №5

#тоже чуть чуть не понял

