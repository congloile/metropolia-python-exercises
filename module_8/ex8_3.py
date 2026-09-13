airports = {}

command = input("What would you like to do with the airport data? ")

while command != "quit":
    if command == "new airport":
        icao = input("Enter ICAO code of the airport: ")
        name = input("Enter airport name: ")
        airports[icao] = name
    elif command == "fetch data":
        icao = input("Enter ICAO code of the airport: ")
        if icao in airports:
            print(airports[icao])
        else: 
            print("No data correspond to this ICAO Code")

    command = input("What would you like to do with the airport data? ")
