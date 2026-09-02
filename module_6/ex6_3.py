number = int(input("Please enter your preferred number to check if there is a prime number: "))

a = 0

for i in range(1, number + 1):
    if number % i == 0:
        a += 1

if a == 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a not prime number.")