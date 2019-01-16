"""
CP1404/CP5632 Practical
Recursion
"""

def calculate_num_of_blocks(n):
    """calculate the number of blocks you will need given the number of rows (n) to make a 2D pyramid"""
    if n <= 0:
        return 0
    return n + calculate_num_of_blocks(n - 1)

def make_2d_pyramid():
    num_of_rows = int(input("How many number of rows? "))
    print("You need {} blocks for {} rows".format(num_of_rows, calculate_num_of_blocks(num_of_rows)))

make_2d_pyramid()