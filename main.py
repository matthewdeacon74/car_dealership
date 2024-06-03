import vehicles as veh

# inventory
motorcycles = [
    veh.Motorcycle('Honda', 1284, 4800, 102),
    veh.Motorcycle('Kawasaki', 3293, 3800, 121),
    veh.Motorcycle('Harley', 10276, 7800, 108),
]
trucks = [
    veh.Truck("Ford", 32186, 9000),
    veh.Truck("Chevrolet", 67983, 4500),
    veh.Truck("Toyota", 22186, 9995),
]

# create container for comparison
vehicles_to_compare = []

# prompt user for specific vehicles to compare
repeat = True
while repeat:
    # prompt user for vehicle type
    while True:
        user_vehicle = input("What type of vehicle do you want to compare (motorcycles or trucks) ? ")
        if user_vehicle == 'motorcycles':
            active_list = motorcycles
            break
        elif user_vehicle == 'trucks':
            active_list = trucks
            break
        else:
            print("Sorry, I didn't understand that.  Do you want to compare (motorcycles or trucks)? ")

    # display list of vehicles of chosen type
    print(f"Here are the available {user_vehicle}:")
    for item in active_list:
        print(f"{active_list.index(item) +1} {item.get_info()}")

    pick_for_compare = input("Would you like to compare one of these vehicles? (y/n) ")

    if pick_for_compare == "y":
        user_choice = input(f"Which of the {user_vehicle} do you wish to compare? (1-{len(active_list)}) ")
        vehicles_to_compare.append(active_list[int(user_choice) - 1])
        print(f"{active_list[int(user_choice) - 1].make} added!")
        active_list.pop(int(user_choice) - 1)

    if len(vehicles_to_compare) > 0:
        compare_now = input(f"Would you like to compare your vehicles now? (y/n)")
        if compare_now == 'y':
            print()
            print("Here are your vehicles to compare:")
            # compare picked vehicles
            for vehicle in vehicles_to_compare:
                print(f" - {vehicle.get_info()}")
                vehicle.make_noise()
            repeat = False
            print("Thank you for shopping with us!")
