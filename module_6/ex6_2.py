numbers = []

number = (input("Please enter your preferred numbers: "))

while number != "":
    number = float(number)
    numbers.append(number)
    number = input("Please enter your next preferred number: ")

numbers.sort(reverse=True)
if len(numbers) >=5:
    print(f"Here are the five greatest numbers sorted in descending order: {numbers[:5]}")
else:
    print("Please enter minimum 5 numbers in total in order to see the result.")
