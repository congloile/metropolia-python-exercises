names = set()

name = input("Please enter a name: ")

while name != "":
    if name in names:
        print("Existing Name")
    else:
       names.add(name)
       print("New Name")

    name = input("Please enter a name: ")

for name in names:
    print(name)
