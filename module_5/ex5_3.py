numbers = []

number = input("Please enter a number: ")
while number != "" :
    number = float(number)
    numbers.append(number)
    number = input("Please enter a number: ")

print("The smallest number is: ", min(numbers))
print("The largest number is: ", max(numbers))
