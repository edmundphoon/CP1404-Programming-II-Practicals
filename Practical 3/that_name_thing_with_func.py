def main():
    name = input("Enter your name: ")
    name = no_blank_name(name)
    print ("Hello World,",name)


def no_blank_name(name):
    while len(name) <= 0:
        print("Blank. Please enter a name.")
        name = input("Enter your name: ")
    return name


def get_name():
    main()


get_name()