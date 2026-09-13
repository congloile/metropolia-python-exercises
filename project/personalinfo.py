import random

def item_rarity():
    rarity = random.randint(1, 100)

    if rarity <= 70:
        return "common"
    elif rarity <= 95:
        return "rare"
    else:
        return "legendary"

def add_item(inventory):
    item = input("What item do you want to add to the inventory? ")
    rarity = item_rarity()
    inventory.append(item + " - " + rarity)

def show_inventory(inventory):
    print(inventory)

def high_scores():
    print("=== HIGH SCORES ===")
    print("Loi: 88")
    print("Anne: 81")
    print("Juha: 67")

inventory = []

name = input("What is your name? ")
age = int(input("How old are you? "))

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
            add_item(inventory)
        elif command == "inventory":  
            show_inventory(inventory)
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


    

    



