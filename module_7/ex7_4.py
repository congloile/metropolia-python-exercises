def getlist(numbers):
    total = 0

    for i in numbers:
        total = total + i

    return sum

def main():
    numbers = [10,89,42,54,78]
    total = getlist(numbers)
    print(total)

main()