import random

def rolldice(sides):
    number = random.randint(1,sides)
    return number

def main():
    sides = int(input("How many sides of a dice do you want to roll? "))

    number = rolldice(sides)

    while number < sides:
        print(number)
        number = rolldice(sides)

main()