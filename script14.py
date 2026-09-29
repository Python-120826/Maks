#дз задание номер 1

class Computer:
    def __init__(self, owner, ram, cpu, hdd, gpu):
        self.owner = owner
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd
        self.gpu = gpu

        def __gt__(self, other):
            return self.ram > other.ram

pc1 = Computer('maksim', 16, 'intel core i9', 1024, 'RTX 5090')
pc2 = Computer('roma', 35, 'intel core i7', 1128, 'RTX 6090')

print(pc1 > pc2)

#дз задание номер 2

class animal:
    def __init__(self, name):
        self.name = name

class birds:
    def __init__(self, color, living_space,wingspan,what_they_eat):
        self.color = color
        self.living_space = living_space
        self.wingspan = wingspan
        self.what_they_eat = what_they_eat
class mammals:
    def __init__(self, color, living_space,size, what_they_eat):
        self.color = color
        self.living_space = living_space
        self.size = size
        self.what_they_eat = what_they_eat
class reptiles:
    def __init__(self, living_space, scale_size, size, what_they_eat):
        self.living_space = living_space
        self.scale_size = scale_size
        self.size = size
        self.what_they_eat = what_they_eat
class fishes:
    def __init__(self, living_space, color, what_they_eat):
        self.living_space = living_space
        self.color = color
        self.what_they_eat = what_they_eat
eagle = birds('white and brown','forest,mountains','1,5m','worms,insects')
chicken = birds('white','nests','1m,0,5m','seeds')

rat = mammals('grey','mink','0,5cm','cheese')
monkey = mammals('brown','jungle','50-70cm','banana')

snake = reptiles('desert','1-2m','3-2m','mice')
chameleon = reptiles('desert','5cm','10cm','insects')

clown_fish = fishes('ocean','orange,white','algae')
great_white_shark = fishes('ocean','grey,white','fishes')

#дз задание номер 3

class figures:
    def __init__(self, triangle,quadrilateral,circle):
        self.triangle = triangle
        self.quadrilateral = quadrilateral
        self.circle = circle

class triangle:
    def __init__(self, a ,b ,c):
        self.a = a
        self.b = b
        self.c = c

width = 3
perimeter = (a + b)*2

class quadrilateral:
    def __init__(self, a, b):
        self.a = a
        self.b = b

width = 4
perimeter = (a + b)*2

class circle:
    def __init__(self, radius_r):
        self.radius_r = radius_r
#дальше не понял как

