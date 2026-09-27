#дз задание номер 1

class computer:
    def __init__(self):
        self.name = 'admin'
        self.ram = 'ram'
        self.processor = 'processor'
        self.disk = 'disk'
        self.video_card = 'video_card'

    def gaming(self):
        print(self.name, 'gaming')
        print(self.ram, 'ram')
        print(self.processor, 'processor')#дальше никак не понял как делать

#дз задание номер 2


class animal:
    def __init__(self):
        self.name = 'birds'
        self.name = 'mammals'
        self.name = 'reptiles'
        self.name = 'fishes'

class birds(animal):
    def color(birds):
        print('black')
    def living_space(birds):
        print('nest')
    def wingspan(birds):
        print('wings')
    def what_they_eat(birds):
        print('insects')

class mammals(animal):
    def color(mammals):
        print('white')
    def living_space(mammals):
        print('cave')
    def size(mammals):
        print('2 meters')
    def what_they_eat(mammals):
        print('grass')

class reptiles(animal):
    def color(reptiles):
        print('blue')
    def living_space(reptiles):
        print('jungle')
    def size(reptiles):
        print('10 meters')
    def what_they_eat(reptiles):
        print('animals')

class fishes(animal):
    def color(fishes):
        print('dark blue')
    def living_space(fishes):
        print('ocean')
    def size(fishes):
        print('1 meter')
    def what_they_eat(fishes):
        print('worm')

birds = 'eagle, chicken'
mammals = 'rat, monkey'
reptiles= 't-rex, spinosaurus'
fishes = 'shark, dolphins'

#дз задание номер 3

class figures:
    def __init__(self):
        self.name = 'triangle'
        self.name = 'quadrilateral'
        self.name = 'circle'

class triangle(figures):
    def side(triangle):
        print('A,B,C')
print('(A + B)x C')

class quadrilateral(figures):
    def side(quadrilateral):
        print('A,B')
print('(A + B)x2')

class circle(figures):
    def side(circle):
        print('Radius R')
print('R x 2')