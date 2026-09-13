import random

def rolldice():
    number = random.randint(1,6)
    return number

def main():
    number = rolldice()

    while number < 6:
        print(number)
        number = rolldice()

main()


