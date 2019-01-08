"""CP1404/CP5632 Practical - Client code to use the Guitars! class."""
# Note that the import has a folder (module) in it.

from Practical_6.guitar import Guitar

def main():
    """Demo test code to show how to use car class."""
    gibson = Guitar("Gibson L-5 CES",1922,16035.40)
    print ("{} ({}) : ${:,.2f}".format(gibson.name, gibson.year, gibson.cost))
    otherGuitar = Guitar("Gibson L-5 CES",2012,1512.9)
    print("{} ({}) : ${:,.2f}".format(otherGuitar.name, otherGuitar.year, otherGuitar.cost))

    print("{} get_age() - Expected 95. Got {:}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 5. Got {:}".format(otherGuitar.name, otherGuitar.get_age()))

    print("{} is_vintage() - Expected True. Got {:}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {:}".format(otherGuitar.name, otherGuitar.is_vintage()))


main()