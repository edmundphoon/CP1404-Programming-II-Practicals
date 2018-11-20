"""
CP1404/CP5632 - Practical# -*- coding: utf-8 -*-
Pseudocode for Shop Calculator

@author: edmundpjc
"""

def main():
    no_of_items = int(input("Enter the number of items: "))
    
    while no_of_items < 0:
        print ("Invalid number of items!")
        no_of_items = int(input("Enter the number of items: "))
    
    print("\n")
    print("Number of items: " + str(no_of_items))
    count = 0
    price_count = 0
    total_price = 0

    for count in range(1, (int(no_of_items) + 1), 1):
        price_of_item = float(input("Enter the price of item " + str(count) + ": "))
        print("Price of item " + str(count) + ": " + str(price_of_item))
        total_price += float(price_of_item)
    print()

    if total_price > 100:
        total_price = (90 / 100) * total_price

    print ("Total price for " + str(no_of_items) + " items is $ {:.2f}".format(total_price))

main()