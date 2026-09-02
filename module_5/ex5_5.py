i = 0

while i < 5:
    name = input("Please enter your username: ")
    passw = input("Please enter your password: ")

    if name == "python" and passw == "rules":
        print("Welcome")
        break

    i += 1

if i == 5:
    print("Access denied")