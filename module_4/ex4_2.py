klasse = input("Please enter your cabin class: ")
if klasse == "LUX":
    print("You have the upper-deck cabin with a balconyy.")
elif klasse == "A":
    print("You have a cabin above the car deck, equipped with a window.")
elif klasse == "B":
    print("You have a windowless cabin above the car deck.")
elif klasse == "C":
    print("You have a windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")