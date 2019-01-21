"""
CP1404/CP5632 Practical
Car Driving Simulator
"""

from Practical_6.car import Car

def menu_display():
    menu = """
    Menu:
    d) drive
    r) refuel
    q) quit
    """
    print(menu)
    return menu


print("Let's drive!")
name = str(input("Enter your car name: "))
new_Car_name = Car(name, fuel=100, odometer=0)

print("{}, fuel={}, odo={}".format(str(new_Car_name.name),str(new_Car_name.fuel),str(new_Car_name.odometer)))
menu_display()
choice = str(input("Enter your choice: ")).lower()

while choice != 'q':
    if choice == 'd':
        drive_km = int(input("How many km do you wish to drive? "))
        if drive_km < 0:
            print("Distance must be >= 0")
            drive_km = int(input("How many km do you wish to drive? "))
        else:
            current_fuel = new_Car_name.fuel - drive_km
            new_Car_name.odometer += drive_km
            if current_fuel > 0:
                new_Car_name.fuel = current_fuel
                print("The car drove {}km.\n".format(str(drive_km)))
            else:
                new_Car_name.fuel = 0
                new_Car_name.odometer = 100
                print("The car drove {}km and ran out of fuel.\n".format(str(drive_km)))
        print("{}, fuel={}, odo={}".format(str(new_Car_name.name), str(new_Car_name.fuel), str(new_Car_name.odometer)))
        menu_display()
        choice = str(input("Enter your choice: ")).lower()

    elif choice == 'r':
        add_fuel = int(input("How many units of fuel do you want to add to the car? "))
        if add_fuel < 0:
            print("Fuel amount must be >= 0")
            add_fuel = int(input("How many units of fuel do you want to add to the car? "))
        else:
            new_Car_name.fuel += add_fuel
            print("Added {} units of fuel\n".format(str(add_fuel)))
        print("{}, fuel={}, odo={}".format(str(new_Car_name.name), str(new_Car_name.fuel), str(new_Car_name.odometer)))
        menu_display()
        choice = str(input("Enter your choice: ")).lower()

    else:
        print ("Invalid choice\n")
        print("{}, fuel={}, odo={}".format(str(new_Car_name.name), str(new_Car_name.fuel), str(new_Car_name.odometer)))
        menu_display()
        choice = str(input("Enter your choice: ")).lower()

print ("Good bye {}'s driver".format(str(name)))