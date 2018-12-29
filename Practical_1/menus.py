"""
CP1404/CP5632 - Practical# -*- coding: utf-8 -*-
Pseudocode for Menus

@author: edmundpjc
"""

#get name
name = input("Enter name: ")

#display menu
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)

#get choice
choice = str(input(">>> ")).upper()

while choice != "Q":
    if choice == "H":
        print("Hello " + str(name))
        print(menu)
        print("\n")
        choice = str(input(">>> ")).upper()
    elif choice == "G":
        print("Goodbye " + str(name))
        print(menu)
        print("\n")
        choice = str(input(">>> ")).upper()
    else:
        print("Invalid choice")
        print(menu)
        print("\n")
        choice = str(input(">>> ")).upper()

print ("Finished.")

