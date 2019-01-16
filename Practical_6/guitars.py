"""
CP1404/CP5632 Practical
Guitars main
"""

from Practical_6.guitar import Guitar

def main():
    guitar_list = []
    print ("My guitars!")
    name = str(input("Name: "))
    while len(name) != 0:
        year = int(input("Year: "))
        if year > 0:
            cost = float(input("Cost: $"))
            if cost > 0:
                new_guitar = Guitar(name,year,cost)
                guitar_list.append(new_guitar)
                print("{} ({}) : ${:,.2f} added.".format(new_guitar.name, new_guitar.year, new_guitar.cost))
                name = str(input("Name: "))
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print ("These are my guitars:")
    vintage_string = ""
    count = 0
    # enumerate function
    for count, guitar in enumerate(guitar_list):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(count + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

main()