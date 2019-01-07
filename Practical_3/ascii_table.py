"""
CP1404/CP5632 - Practical
ASCII Table

@author: edmundpjc
"""

LOWER = 33
UPPER = 127

def display_menu():
    return menu

def get_number(lower, upper):
    print ("Enter a number between", lower, "and", upper, ": ")
    get_num = int(input(">>> "))
    while (get_num < lower) or (get_num > upper):
        print ("Please enter a valid number!")
        print("Enter a number between", lower, "and", upper, ": ")
        get_num = int(input(">>> "))
    print ("The character for", str(get_num), "is", str(chr(get_num)))

def main():
    menu = """
            Enter 1 to show ASCII table
            Enter 2 to get ASCII value of character
            Enter 3 to get character value of ASCII
            Enter 4 to Quit
            """
    print(menu)
    choice = int(input(">>> "))
    while choice != 4:
        if choice == 1:
            i = 0
            print ("chr     ord")
            print ("-----------")
            for i in range(LOWER,UPPER,1):
                print ("{:3}    {:}".format(str(i),str(chr(i))))
            print(menu)
            choice = int(input(">>> "))
        elif choice == 2:
            get_character = str(input("Enter a character: "))
            if len(get_character) == 0:
                print("Field must not be blank.")
                get_character = str(input("Enter a character: "))
            if int(ord(get_character)) < LOWER or int(ord(get_character)) > UPPER:
                print("No such value")
                get_character = str(input("Enter a character: "))
            elif int(ord(get_character)) > LOWER or int(ord(get_character)) < UPPER:
                print("The ASCII code for", str(get_character), "is", str(ord(get_character)))
            else:
                print("No such value")
                get_character = str(input("Enter a character: "))
            print(menu)
            choice = int(input(">>> "))
        elif choice == 3:
            min_num = 0
            while (min_num < 10) or (min_num > 50):
                try:
                    min_num = int(input("Enter a number (10-50): "))
                except ValueError:
                    print("Please enter a valid number!")
                    min_num = int(input("Enter a number (10-50): "))
            max_num = 0
            while (max_num < 10) or (max_num > 50):
                try:
                    max_num = int(input("Enter a number (10-50): "))
                except ValueError:
                    print("Please enter a valid number!")
                    max_num = int(input("Enter a number (10-50): "))
            if max_num > min_num:
                get_number(min_num, max_num)
            else:
                print("Error! The second number must not be smaller than the first number. Please try again.")
            print(menu)
            choice = int(input(">>> "))
        else:
            print("Invalid choice! Please try again.")
            print(menu)
            choice = int(input(">>> "))
    print ("Goodbye")

main()