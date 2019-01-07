"""
@author: edmundpjc
"""

LOWER = 33
UPPER = 127

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
                print ("Field must not be blank.")
                get_character = str(input("Enter a character: "))
            if int(ord(get_character)) < LOWER or int(ord(get_character)) > UPPER:
                print ("No such value")
                get_character = str(input("Enter a character: "))
            elif int(ord(get_character)) > LOWER or int(ord(get_character)) < UPPER:
                print("The ASCII code for", str(get_character), "is", str(ord(get_character)))
            else:
                print ("No such value")
                get_character = str(input("Enter a character: "))
            print(menu)
            choice = int(input(">>> "))
        elif choice == 3:
            get_num = int(input("Enter a number between 33 and 127: "))
            while get_num < LOWER or get_num > UPPER:
                print ("Error. Second number is lower than first number.")
                get_num = int(input("Enter a number between 33 and 127: "))
            print ("The character for", str(get_num), "is", str(chr(get_num)))
            print(menu)
            choice = int(input(">>> "))
        else:
            print("Invalid choice! Please try again.")
            print(menu)
            choice = int(input(">>> "))
    print ("Goodbye")

main()