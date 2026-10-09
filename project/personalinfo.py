import json
import random
from unicodedata import name
from item import Item
import player
from room import Room
from player import Player 

def show_intro():
    with open("intro.txt", "r", encoding="utf-8") as file:
        print(file.read())

def show_instructions():
    with open("instructions.txt", "r", encoding="utf-8") as file:
        print(file.read())

def show_about():
    with open("about.txt", "r", encoding="utf-8") as file:
        print(file.read())

def show_inventory(player):
    if not player.items:
        print("\nYour inventory is empty.")
        return

    print("\nInventory:")

    for item in player.items:
        print(f"- {item.name}")

# Check if a player profile already exists
def player_exists(name):
    try:
        with open("savegames.json", "r", encoding="utf-8") as file:
            savegames = json.load(file)
    except FileNotFoundError:
        return False

    return name in savegames

# Show the player's current room and any item in it
def show_room(player):
    print(f"\nYou are in the {player.location.name}.")

    if player.location.item is not None:
        print(f"You see: {player.location.item.name}")
    else:
        print("There is no item here.")

# Let the player choose one of the available game routes
def choose_activity():
    activity = input("Choose activity: 'jogging', 'work' or 'shopping': ")

    while activity not in ["jogging", "work", "shopping"]:
        activity = input("Please type 'jogging', 'work' or 'shopping': ")

    return activity

# Restore the original items when starting or loading a game
def reset_rooms(rooms):
    for room in rooms:
        if room.name == "Hall":
            room.item = Item("Shoes")

        elif room.name == "Kitchen":
            room.item = Item("Key")

        elif room.name == "Bedroom":
            room.item = Item("Phone")

        elif room.name == "Living Room":
            room.item = Item("Laptop")

def move_player(player, rooms):
    print("\nAvailable rooms:")

    for room in rooms:
        if room.name == "Living Room":
            print("- Living Room (type 'liv')")
        else:
            print(f"- {room.name}")

    destination_name = input("Where do you want to go? ").lower()

    if destination_name == "liv":
        destination_name = "living room"

    for room in rooms:
        if room.name.lower() == destination_name:

            if room == player.location:
                return

            player.move(room)
            print(f"You moved to the {room.name}.")
            return

    print("Room not found.")

# Show the player's current room and any item in it
def eco_action(player):
    room_name = player.location.name

    if room_name in player.eco_actions:
        print("You already completed the eco action in this room.")
        return
    
    if room_name == "Hall":
        print("You turned off the light.")

    elif room_name == "Kitchen":
        print("You took the waste out for recycling.")

    elif room_name == "Bedroom":
        print("You turned off the fan.")

    elif room_name == "Living Room":
        print("You turned off the TV.")

    player.eco_actions.append(room_name)

# Save multiple player profiles in one JSON file
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
        "eco_actions": player.eco_actions,
        "items": []
    }

    for item in player.items:
        savegames[player.name]["items"].append({
            "name": item.name
        })

    with open("savegames.json", "w", encoding="utf-8") as file:
        json.dump(savegames, file, indent=4)

    print(f"Game saved.")

# Restore the selected player's saved game state
def load_game(rooms):
    with open("savegames.json", "r", encoding="utf-8") as file:
        savegames = json.load(file)

        reset_rooms(rooms)

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
    player.eco_actions = data["eco_actions"]

    for item_data in data["items"]:
        item = Item(item_data["name"])
        player.items.append(item)

# Restore the selected player's saved game state
    for room in rooms:
        for item in player.items:
            if room.item is not None and room.item.name == item.name:
                room.item = None

    print("Game loaded.")

    return player

# Main gameplay loop
def game_loop(player, rooms):
    while True:
        show_room(player)

        print("\n=== GAME MENU ===")
        print("move")
        print("collect")
        print("eco action (type 'eco')")
        print("save")
        print("load")
        print("inventory")
        print("menu")

        action = input("What do you want to do? ")

        if action == "move":
            move_player(player, rooms)

        elif action == "collect":
            player.collect_item()

        elif action == "eco":
            eco_action(player)

        elif action == "inventory":
            show_inventory(player)

        elif action == "save":
            save_game(player)

        elif action == "load":
            loaded_player = load_game(rooms)

            if loaded_player is not None:
                player = loaded_player
                print(f"Welcome back, {player.name}!")
                print(f"Your activity is: {player.activity.capitalize()}.")


        elif action == "menu":
            break

        if player.location.name == "Hall" and check_win(player):
            print("\nYou are ready to leave!")

            leave_now = input("Do you want to leave now? (yes/no): ").lower()

            if leave_now == "yes":
                print("You completed your objective.")

                final_score = calculate_score(player)
                print(f"Final score: {final_score}")

                update_high_score(player, final_score)
                break

            else:
                print("You can continue exploring or complete more eco actions.")

# Checks whether the player has a specific item in their inventory
def has_item(player, item_name):
    for item in player.items:
        if item.name == item_name:
            return True

    return False

# Check route-specific win conditions
def check_win(player):
    has_key = has_item(player, "Key")
    has_shoes = has_item(player, "Shoes")
    has_phone = has_item(player, "Phone")
    eco_count = len(player.eco_actions)

    if player.activity == "jogging":
        return has_key and has_shoes and eco_count >= 3

    elif player.activity == "work":
        return has_key and has_shoes and eco_count >= 2

    elif player.activity == "shopping":
        return has_key and has_shoes and has_phone and eco_count >= 1

    return False

# Calculate the final score based on eco actions and item choices
def calculate_score(player):
    score = 60

    score += len(player.eco_actions) * 10

    if player.activity == "jogging":
        if has_item(player, "Laptop"):
            score -= 10

        if has_item(player, "Phone"):
            score -= 5

    elif player.activity == "work":
        if not has_item(player, "Phone"):
            score -= 10

        if not has_item(player, "Laptop"):
            score -= 5
    elif player.activity == "shopping":
        if has_item(player, "Laptop"):
            score -= 15

    return score

# Update the player's high score only if the new score is higher
def update_high_score(player, score):
    try:
        with open("highscores.json", "r", encoding="utf-8") as file:
            high_scores = json.load(file)
    except FileNotFoundError:
        high_scores = {}

    if player.name not in high_scores or score > high_scores[player.name]:
        high_scores[player.name] = score

        with open("highscores.json", "w", encoding="utf-8") as file:
            json.dump(high_scores, file, indent=4)

def high_scores():
    try:
        with open("highscores.json", "r", encoding="utf-8") as file:
            scores = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No high scores yet.")
        return

    print("\n=== HIGH SCORES ===")

    for name, score in sorted(scores.items(), key=lambda item: item[1], reverse=True):
        print(f"{name}: {score}")

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
print("high scores (type 'high')")
print("about")
print("lopeta")
command = input("Please enter your command: ")
while command != "lopeta":
    if command == "play":
        choice = input("New game or continue? Type 'new' or 'cont': ")

        if choice == "new":
            show_intro()

            while True:
                name = input("What is your name? ")

                if player_exists(name):
                    print("This player already exists. Please choose another name.")
                else:
                    break

            age = int(input("How old are you? "))

            reset_rooms(rooms)

            player = Player(name, age, hall)

            print(f"Hello, {player.name}!")

            activity = choose_activity()
            player.activity = activity

            game_loop(player, rooms)

    elif command == "instructions":
        show_instructions()
    elif command == "high":
        high_scores()
    elif command == "about":
        show_about()
         
    print("\n=== MAIN MENU ===")
    print("play")
    print("instructions")
    print("high scores (type 'high')")
    print("about")
    print("lopeta")

    command = input("Please enter your command: ")


    

    



