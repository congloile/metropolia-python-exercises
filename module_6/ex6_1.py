dice = int(input("How many dice would you like to roll? "))

total = 0

import random

for i in range(dice):
    number = random.randint(1, 6)
    total = total + number

print(f"The sum of the numbers after rolling the dice is: {total}")

