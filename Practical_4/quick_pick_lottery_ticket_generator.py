"""
CP1404/CP5632 Practical
“Quick Pick” Lottery Ticket Generator
"""

import random

num_of_picks = int(input("How many quick picks? "))

row = 0

row_count = 0

for row in range(num_of_picks):
    num1 = random.randint(1, 45)
    num2 = random.randint(1, 45)
    num3 = random.randint(1, 45)
    num4 = random.randint(1, 45)
    num5 = random.randint(1, 45)
    num6 = random.randint(1, 45)
    print ("{:-2} {:-2} {:-2} {:-2} {:-2} {:-2}".format(int(num1),int(num2),int(num3),int(num4),int(num5),int(num6)))
    row += 1