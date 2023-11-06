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
