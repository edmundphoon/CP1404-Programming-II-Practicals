"""
CP1404/CP5632 - Practical# -*- coding: utf-8 -*-
Pseudocode for Menu-driven number sequence generator

@author: edmundpjc
"""

def menu():
    # display menu
    display_menu = """
        (1) Show the even numbers from 1st to 2nd number
        (2) Show the odd numbers from 1st to 2nd number
        (3) Show the squares from 1st to 2nd number
        (4) Exit the program
        """
    print (display_menu)

#even numbers
def even_num(x, y, i):
    for i in range(x, y+1, i):
        if int(i % 2) == 0:
            print (int(i), end =" ")

#odd numbers
def odd_num(x, y, i):
    for i in range(x, y+1, i):
        if int(i % 2) != 0:
            print (int(i), end =" ")

#square
def sqr_num(x, y, i):
    for i in range(x, y+1, i):
        print (int(i**2), end =" ")

def main():
    #get x input
    x = int(input("Enter 1st number: "))

    #get y input
    y = int(input("Enter 2nd number: "))

    while x > y:
        print ("\nError. The 2nd number must be less than the 1st number.")
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))

    i = 0

    menu()

    # get choice
    choice = int(input(">>> "))

    while choice != 4:
        if choice == 1:
            even_num(x, y, 1)
            menu()
            choice = int(input(">>> "))
        elif choice == 2:
            odd_num(x, y, 1)
            menu()
            choice = int(input(">>> "))
        elif choice == 3:
            sqr_num(x, y, 1)
            menu()
            choice = int(input(">>> "))
        else:
            print("Invalid choice")
            menu()
            choice = int(input(">>> "))

    print ("Goodbye.")

main()