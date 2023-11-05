import random
import time

print("Start game")

print("Введите имя персонажа")
name = input()
# Имя гг

print("Выберите уровень сложности")
print ("1 - легкий      2 - средний         3 - сложный")
lvl_game = int(input())
# Уровень сложности !!!Нужно переделать !!!невозможно выжить!!! !!!


attack_user = 10
healing_user = 100
# Базовые характеристики гг
# Надо сделать систему брони %-ную

# Класс для хранения информации об элементе инвентаря
class Item:
    def __init__(self, name, description, weight, value):
        self.name = name
        self.description = description
        self.weight = weight
        self.value = value

# Класс для хранения инвентаря игрока
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name == item_name:
                self.items.pop(i)
                return

    def get_items(self):
        return self.items

    def get_item_by_name(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def get_item_count(self, item_name):
        item_count = 0
        for item in self.items:
            if item.name == item_name:
                item_count += 1
        return item_count
    #  Ограничить место инвентаря

    # Функция для отображения инвентаря игрока
    def show_inventory(inventory):
        print("Ваш инвентарь:")
        for item in inventory.items:
            print(f"{item.name}: {item.description} (вес {item.weight}, цена {item.value})")
inventory = Inventory()

# ПИВО
beer = Item("Пиво", "Восстанавливает 10 здоровья, но точность уменьшается", 1, 10)
inventory.add_item(beer)

# Нужно добавить инвентарь и полноценное использование. Тут должны быть хилки, перки, инструменты, оружие, !!!СВЯЩЕННЫЙ КРЕСТЬ!!!, ну и т.д. !+- сделал!


# Противники
class Goblin(object):
    def __init__(self):
        self.name = "Гоблин"
        self.description = "Маленький, но злобный монстр"
        self.attack = 5 * lvl_game
        self.health = 10

class Troll(object):
    def __init__(self):
        self.name = "Тролль"
        self.description = "Большой и сильный монстр"
        self.attack = 10 * lvl_game
        self.health = 35

class Dragon(object):
    def __init__(self):
        self.name = "Дракон"
        self.description = "Огненное чудовище"
        self.attack = 20 * lvl_game
        self.health = 50

class Zombie(object):
    def __init__(self):
        self.name = "Зомби"
        self.description = "Слабый противник, но не похоже, что он собирается сдаваться"
        self.attack = 5 * lvl_game
        self.health = 25

class Dvorf(object):
    def __init__(self):
        self.name = "Дворф"
        self.description = "Главный любитель пива. За пиво и двор - может убить каждого"
        self.attack = 7 * lvl_game
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

# Случайный выбор противника
def random_enemy():
    # Список доступных противников
    enemies = [goblin, troll, dragon, zombie, dvorf]

    # Случайный выбор противника
    enemy = random.choice(enemies)

    return enemy

# Вывод противника
enemy = random_enemy()

# Нужно добавить сюда элементы перемещения, движения для простоты будет выглядеть как прыжки по ячейкам, и построить карту с сундуками, врагами, сохранением и т.п.

print(f"Вы встретили монстра - {enemy.name}")
print("БОЙ")
time.sleep(2)
battle =  1
# Мы пришли на точку с монстром и переменной станет 1, по окончанию боя она станет 0. Когда мы дойдем до следующей точки она снова станет 1

# !!!!Добавить случайный выбор противника и настроить выход из цикла, при смерти одной из сторон
while battle == 1:

    print("Выберите действие")
    print("1 - Атака        2 - Инвентарь        3 - Убежать")
    boi = int(input())

    if boi == 1:
        def dice(sides=6):
            return random.randint(1, sides)


        def fight(attack_damage, defender_healing, attack_name, defender_name):
            cube = dice(10)
            if cube == 1:
                print(f"{attack_name} промахнулся")
                time.sleep(2)
            elif cube == 10:
                defender_healing -= attack_damage * 2
                print(f"{defender_name} осталось {defender_healing} здоровья *критический урон*")
                time.sleep(2)
            else:
                defender_healing -= attack_damage
                print(f"{defender_name} осталось {defender_healing} здоровья")
                time.sleep(2)
            return defender_healing
        


        if healing_user > 0 and enemy.health > 0:
            enemy.health = fight(attack_user, enemy.health, name, enemy.name)
            healing_user = fight(enemy.attack, healing_user, enemy.name, name)

        if healing_user <= 0 or enemy.health <= 0:
            battle = 0
    # Расчет урона методом кубика + задержка времени при подсчёте урона
    # Добавить в боёвку вариативность, как в с Дворфом. Например, босса Дракона можно будет задобрить с помощью какой-нибудь хренью, которая занимает большую часть инвенторя.
    elif boi == 2:
        print(Inventory.show_inventory(inventory))
        choice = input()
        if choice == beer and enemy == dvorf:
            enemy.is_drunk = True
            print(f"Дворф выпил пиво и стал добрым")
            print(f"Дворф: 'Ну ладно, давай договоримся. Я не буду тебя трогать, если ты мне дашь ещё пива.'")
            choice = input()
            if choice == beer:
                print(f"Дворф: 'Спасибо, приятель. Я тебе ещё отплачу.'")
                enemy.health = 100
                battle = 0
            else:
                print(f"Дворф: 'Ну ладно, тогда я тебя убью.'")
    # Пиво не работает

    # Тут взаимодействие с инвентарём во время боя

    else:
        print(f"Вы сбежали с поля боя, но вы сохранили свою жизнь. Ваше здоровье {healing_user}")
        battle = 0
    # Интересная механика. Игрок в любой момент может спасти свою жизнь или попробовать пойди по другому пути, мб полутать сундуки


# Надо запихнуть священный крест, который будет убивать врагов моментально, но ограничить кол-во использования

# Что бы это работало как надо пива!!!
# Если интерес останется, можно перенести этот код на C# или С++, С# - unity. Как вариант, можно будет за тлить платформы