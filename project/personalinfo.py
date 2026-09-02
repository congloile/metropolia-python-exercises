name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print("You are a minor")
else:
    print(f"Hello {name}")

    print("\n=== MAIN MENU ===")
    print("play")
    print("instructions")
    print("about")
    print("lopeta")
    command = input("Please enter your command: ")
    while command != "lopeta":
        if command == "play":
            print("Starting the game")
        elif command == "instructions":
            print("Here are the instructions for this game:... ")
        elif command == "about":
            print("About this game and developer:... ")
        
        print("\n=== MAIN MENU ===")
        print("play")
        print("instructions")
        print("about")
        print("lopeta")

        command = input("Please enter your command: ")
    



