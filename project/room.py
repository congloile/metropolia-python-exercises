from item import Item

class Room:
    def __init__(self, name: str, item: Item = None):
        self.name = name
        self.item = item

