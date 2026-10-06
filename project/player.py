from item import Item
from room import Room

class Player:
    def __init__(self, name: str, age: int, location: Room):
        self.name = name
        self.age = age
        self.items: list[Item] = []
        self.location = location

    def move(self, destination: Room):
        self.location = destination

    def collect_item(self):
        item = self.location.item

        if item is not None:
            self.items.append(item)
            self.location.item = None
            print(f"You collected: {item.name}")