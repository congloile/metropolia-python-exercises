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


def show_inventory(player):
    for item in player.items:
        print(item.name)

def show_room(player):
    print(f"\nYou are in the {player.location.name}.")

    if player.location.item is not None:
        print(f"You see: {player.location.item.name}")
    else:
        print("There is no item here.")

def choose_activity():
    activity = input("Choose activity: 'jogging' or 'work': ")

    while activity != "jogging" and activity != "work":
        activity = input("Please type 'jogging' or 'work': ")

    return activity

def save_game(player):
    try:
        with open("savegames.json", "r", encoding="utf-8") as file:
            savegames = json.load(file)
    except FileNotFoundError:
        savegames = {}

    savegames[player.name] = {
        "age": player.age,
        "activity": player.activity,
        "location": player.location.name,
        "items": []
    }

    for item in player.items:
        savegames[player.name]["items"].append({
            "name": item.name
        })

    with open("savegames.json", "w", encoding="utf-8") as file:
        json.dump(savegames, file, indent=4)

    print(f"Game saved.")

def load_game(rooms):
    with open("savegames.json", "r", encoding="utf-8") as file:
        savegames = json.load(file)

    print("\nSaved players:")

    for name in savegames:
        print(f"- {name}")

    selected_name = input("Choose a player: ")

    if selected_name not in savegames:
        print("Player not found.")
        return None

    data = savegames[selected_name]

    location = rooms[0]

    for room in rooms:
        if room.name == data["location"]:
            location = room

    player = Player(selected_name, data["age"], location)
    player.activity = data["activity"]

    for item_data in data["items"]:
        item = Item(item_data["name"])
        player.items.append(item)

    print("Game loaded.")

    return player

def game_loop(player):
    while True:
        show_room(player)

        print("\n=== GAME MENU ===")
        print("collect")
        print("inventory")
        print("menu")

        action = input("What do you want to do? ")

        if action == "collect":
            player.collect_item()

        elif action == "inventory":
            show_inventory(player)

        elif action == "menu":
            break

def high_scores():
    print("=== HIGH SCORES ===")
    print("Loi: 88")
    print("Anne: 81")
    print("Juha: 67")

shoes = Item("Shoes")
key = Item("Key")
phone = Item("Phone")
laptop = Item("Laptop")

hall = Room("Hall", shoes)
kitchen = Room("Kitchen", key)
bedroom = Room("Bedroom", phone)
living_room = Room("Living Room", laptop)

rooms = [hall, kitchen, bedroom, living_room]

print("\n=== MAIN MENU ===")
print("play")
print("instructions")
print("inventory")
print("save")
print("high scores")
print("about")
print("lopeta")
command = input("Please enter your command: ")
while command != "lopeta":
    if command == "play":
        choice = input("New game or continue? Type 'new' or 'cont': ")

        if choice == "new":
            show_intro()

            name = input("What is your name? ")
            age = int(input("How old are you? "))

            player = Player(name, age, hall)

            print(f"Hello, {player.name}!")

            activity = choose_activity()
            player.activity = activity
            
            game_loop(player)

        elif choice == "cont":
            print("Loading...")
            player = load_game(rooms)

            if player is not None:
                print(f"Welcome back, {player.name}!")
                print(f"You are going {player.activity}.")
                game_loop(player)

    elif command == "instructions":
            show_instructions()
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
    print("inventory")
    print("save")
    print("high scores")
    print("about")
    print("lopeta")

    command = input("Please enter your command: ")


    

    



