"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def cel_to_fah():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fah_to_cel():
    global fahrenheit, celsius
    # TODO: Write this section to convert F to C and display the result
    fahrenheit = float(input("Fahrenheit temperature: "))
    # Hint: celsius = 5 / 9 * (fahrenheit - 32)
    celsius = 5 / 9 * (fahrenheit - 32)
    # Remove the "pass" statement when you are done. It's a placeholder.
    # pass
    print("Result: {:.2f} C".format(celsius))


while choice != "Q":
    if choice == "C":
        cel_to_fah()
    elif choice == "F":
        fah_to_cel()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")