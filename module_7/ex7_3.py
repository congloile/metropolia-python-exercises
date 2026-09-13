def conversion(gallons):
    liters = gallons * 3.78541
    return liters

def main():
    gallons = int(input("How many gallons do you want to convert? "))
    while gallons >= 0:
        liters = conversion(gallons)
        print(gallons, "gallons equal to", liters, "liters")

        gallons = int(input("How many gallons do you want to convert? "))

main()