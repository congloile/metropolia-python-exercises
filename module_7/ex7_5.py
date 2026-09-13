def getlist(numbers):
    new_list = []

    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)

    return new_list

def main():
    numbers = [34,62,346,324,745,423]
    new_list = getlist(numbers)
    print(new_list)

main()