tal = float(input("Please enter talents: "))
pds = float(input("Pleas enter pounds: "))
lts = float(input("Please enter lots: "))
taltog = tal*20*32*13.3
pdstog = pds*32*13.3
ltstog = lts*13.3
total = taltog + pdstog + ltstog
print(f"The weight in modern units is: {total} grams")