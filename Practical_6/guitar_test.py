"""CP1404/CP5632 Practical - Client code to use the Guitars! class."""
# Note that the import has a folder (module) in it.

from Practical_6.guitar import Guitar

def main():
    """Demo test code to show how to use car class."""
    gibson = Guitar("Gibson L-5 CES",1922,16035.40)
    print ("{} ({}) : ${:,.2f}".format(gibson.name, gibson.year, gibson.cost))
    otherGuitar = Guitar("Gibson L-5 CES",2012,16035.40)
    print("{} ({}) : ${:,.2f}".format(otherGuitar.name, otherGuitar.year, otherGuitar.cost))

    print("{} get_age() - Expected {:}. Got {:}".format(gibson.name, gibson.get_age(), gibson.get_age()))
    print("{} get_age() - Expected {:}. Got {:}".format(otherGuitar.name, otherGuitar.get_age(), otherGuitar.get_age()))

    print("{} is_vintage() - Expected {:}. Got {:}".format(gibson.name, gibson.is_vintage(), gibson.is_vintage()))
    print("{} is_vintage() - Expected {:}. Got {:}".format(otherGuitar.name, otherGuitar.is_vintage(), otherGuitar.is_vintage()))


main()