tal = float(input("Please enter talents: "))
pds = float(input("Pleas enter pounds: "))
lts = float(input("Please enter lots: "))
taltog = tal*20*32*13.3
pdstog = pds*32*13.3
ltstog = lts*13.3
total = taltog + pdstog + ltstog
kg = total // 1000
grams = total % 1000
if kg == 1:
    print(f"The weight in modern units is: {kg:.0f} kilogram and {grams:.2f} grams.")
else:
    print(f"The weight in modern units is: {kg:.0f} kilograms and {grams:.2f} grams.")