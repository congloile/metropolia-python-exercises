import math

def pizza(diameter,price):
    radius_in_m = diameter/2/100
    area = math.pi * radius_in_m **2
    priceperm2 = price/area
    return priceperm2

def main():
    diameter1 = float(input("Please enter the diameter of the first pizza: "))
    price1 = float(input("Please enter the price of the first pizza: "))
    diameter2 = float(input("Please enter the diameter of the second pizza: "))
    price2 = float(input("Please enter the price of the second pizza: "))
    priceperm2_1 = pizza(diameter1, price1)
    priceperm2_2 = pizza(diameter2, price2)
    if priceperm2_1 > priceperm2_2:
        print("The second pizza provides better value for money.")
    elif priceperm2_1 < priceperm2_2:
        print("The first pizza provides better value for money.")
    else:
        print("Both pizzas provide equal value for money.")

main()