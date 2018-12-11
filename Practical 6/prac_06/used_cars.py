"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        """
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.
        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
         return "Car, fuel = {}, odometer = {}".format(str(self.fuel), str(self.odometer))



#from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car(100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))


main()