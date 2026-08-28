length = float(input("How long is the zander in cm? "))
limit = 42 - length
if length < 42:
    print(f"Please  release the fish back into the lake. The fish is {limit} cm below the size limit caught fish.")
else:
    print("The fish meets the size limit. You can keep the fish.")

