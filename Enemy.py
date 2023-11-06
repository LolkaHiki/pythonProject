# Противники
import main


class Goblin(object):
    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленький, но злобный монстр"
        self.attack = 5 * main.lvl_game
        self.health = 10

class Troll(object):
    def __init__(self):
        self.name = "Тролль"
        self.description = "Большой и сильный монстр"
        self.attack = 10 * main.lvl_game
        self.health = 35

class Dragon(object):
    def __init__(self):
        self.name = "Дракон"
        self.description = "Огненное чудовище"
        self.attack = 20 * main.lvl_game
        self.health = 50

class Zombie(object):
    def __init__(self):
        self.name = "Зомби"
        self.description = "Слабый противник, но не похоже, что он собирается сдаваться"
        self.attack = 5 * main.lvl_game
        self.health = 25

class Dvorf(object):
    def __init__(self):
        self.name = "Дворф"
        self.description = "Главный любитель пива. За пиво и двор - может убить каждого"
        self.attack = 7 * main.lvl_game
        self.health = 30
        self.is_drunk = False

    def drink_beer(self):
        self.is_drunk = True
        print(f"Дворф выпил пиво и стал добрым")
        # Дворф очень любит пиво, если ему дать пиво во время боя - то он станет к гг добрым
    #починить зомби, он ломает всё

goblin = Goblin()
troll = Troll()
dragon = Dragon()
zombie = Zombie()
dvorf = Dvorf()
