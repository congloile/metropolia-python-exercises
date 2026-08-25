gender = input("What is your biological gender? ")
hemo = float(input("What is your hemoglobin value (g/l)?"))
if gender == "male":
    if hemo < 134:
        print("Your hemoglobin value is below the normal range")
    elif hemo > 167:
        print("Your hemoglobin value is above the normal range")
    else:
        print("Your hemoglobin value is normal")
elif gender == "female":
    if hemo < 117:
            print("Your hemoglobin value is below the normal range")
    elif hemo > 155:
            print("Your hemoglobin value is above the normal range")
    else:
            print("Your hemoglobin value is normal")
