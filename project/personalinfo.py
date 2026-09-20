import random
from item import Item
from room import Room
from player import Player 

def item_rarity():
    rarity = random.randint(1, 100)

    if rarity <= 70:
        return "common"
    elif rarity <= 95:
        return "rare"
    else:
        return "legendary"

def add_item(player):
    name = input("What item do you want to add? ")
    weight = float(input("What is the item's weight? "))

    item = Item(name, weight)
    player.items.append(item)

def show_inventory(player):
    for item in player.items:
        print(item.name, "-", item.weight, "kg")

def high_scores():
    print("=== HIGH SCORES ===")
    print("Loi: 88")
    print("Anne: 81")
    print("Juha: 67")

key = Item("Key", 0.1)
phone = Item("Phone", 0.2)

hall = Room("Hall", key)
kitchen = Room("Kitchen")
bedroom = Room("Bedroom", phone)

name = input("What is your name? ")
age = int(input("How old are you? "))

player = Player(name, hall)
inventory = player.items

print(f"Name: {name}")
print(f"Age: {age}")

if age < 12:
    print("You are a minor")
else:
    print(f"Hello {name}")

    print("\n=== MAIN MENU ===")
    print("play")
    print("instructions")
    print("add item")
    print("inventory")
    print("high scores")
    print("about")
    print("lopeta")
    command = input("Please enter your command: ")
    while command != "lopeta":
        if command == "play":
            print("Starting the game")
        elif command == "instructions":
            print("Here are the instructions for this game:... ")
        elif command == "add item":
            add_item(player)
        elif command == "inventory":  
            show_inventory(player)
        elif command == "high scores":
            high_scores()
        elif command == "about":
            print("About this game and developer:... ")
         
        print("\n=== MAIN MENU ===")
        print("play")
        print("instructions")
        print("add item")
        print("inventory")
        print("high scores")
        print("about")
        print("lopeta")

        command = input("Please enter your command: ")


    

    



