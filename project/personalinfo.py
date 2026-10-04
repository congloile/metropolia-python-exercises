import json
import random
from item import Item
from room import Room
from player import Player 

def show_intro():
    with open("intro.txt", "r", encoding="utf-8") as file:
        print(file.read())

def show_instructions():
    with open("instructions.txt", "r", encoding="utf-8") as file:
        print(file.read())

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

    item = Item(name, weight)
    player.items.append(item)

def show_inventory(player):
    for item in player.items:
        print(item.name)

def save_game(player):
    data = {
        "name": player.name,
        "age": player.age,
        "location": player.location.name,
        "items": []
    }

    for item in player.items:
        data["items"].append({
            "name": item.name,
            "weight": item.weight
        })

    with open("savegame.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Game saved.")

def load_game(rooms):
    with open("savegame.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    location = rooms[0]

    for room in rooms:
        if room.name == data["location"]:
            location = room

    player = Player(data["name"], data["age"], location)

    for item_data in data["items"]:
        item = Item(item_data["name"], item_data["weight"])
        player.items.append(item)

    print("Game loaded.")

    return player

def high_scores():
    print("=== HIGH SCORES ===")
    print("Loi: 88")
    print("Anne: 81")
    print("Juha: 67")

key = Item("Key")
phone = Item("Phone")

hall = Room("Hall", key)
kitchen = Room("Kitchen")
bedroom = Room("Bedroom", phone)
rooms = [hall, kitchen, bedroom]

choice = input("New game or continue? Type 'new' or 'cont': ")

if choice == "new":
    show_intro()

    name = input("What is your name? ")
    age = int(input("How old are you? "))

    player = Player(name, age, hall)

elif choice == "cont":
    print("Loading...")
    player = load_game(rooms)

print(f"Name: {player.name}")
print(f"Age: {player.age}")

if age < 12:
    print("You are a minor")
else:
    print(f"Hello {name}")

    print("\n=== MAIN MENU ===")
    print("play")
    print("instructions")
    print("add item")
    print("inventory")
    print("save")
    print("high scores")
    print("about")
    print("lopeta")
    command = input("Please enter your command: ")
    while command != "lopeta":
        if command == "play":
            print("Starting the game")
        elif command == "instructions":
            show_instructions()
        elif command == "add item":
            add_item(player)
        elif command == "inventory":  
            show_inventory(player)
        elif command == "save":
            save_game(player)
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


    

    



