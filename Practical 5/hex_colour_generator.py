"""
CP1404/CP5632 Practical
Hexadecimal colour generator
"""

HEX_COLOUR = {"Red": "#ff0000", "Orange": "#ffa500", "Yellow": "#ffff00", "Green": "#00ff00",
               "Blue": "#0000ff", "Purple": "#a020f0", "Cyan": "#00ffff", "White": "#ffffff",
              "Black": "#000000", "Pink": "#ffc0cb", "Gray": "#bebebe", "Brown": "#a52a2a"}

colour = input("Enter colour: ")
while colour != "":
    if colour.title() in HEX_COLOUR:
        print(colour.title(), "is", HEX_COLOUR[colour.title()])
    elif colour.title() == "All":
        for colour in HEX_COLOUR:
            print (colour + "  is " + HEX_COLOUR[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")
