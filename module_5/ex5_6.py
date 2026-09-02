import random

number = int(input("How many random points do you want to generate? "))

i = 0
n = 0

while i < number:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        n += 1

    i += 1

pi = (4*n) / number

print(f"The approximately value of pi is {pi}")


