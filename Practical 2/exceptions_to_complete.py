"""
CP1404/CP5632 - Practical 2
Fill in the TODOs to complete the task

@author: edmundpjc
"""

finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        get_integer = int(input("Type a number: "))
        # TODO: this line
        finished = True
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)