"""
CP1404/CP5632 - Practical
Pseudocode for Sales Bonus
"""

def main():
    sales = float(input("Enter sales: $"))
    bonus = 0

    #loop to make program repeat for user's sales until they enter a negative no.
    while sales >= 0:
        if sales < 1000:
            bonus = float(sales) * (10 / 100)
        else:
            bonus = float(sales) * (15 / 100)

        output = float(sales) - float(bonus)

        print("Expected bonus: " + str(bonus))
        print("Expected output: " + str(output))

        print("\n")
        sales = float(input("Enter sales: $"))

main()