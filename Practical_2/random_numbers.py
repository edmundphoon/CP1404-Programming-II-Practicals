"""
CP1404/CP5632 - Practical_2
Pseudocode for Random numbers

@author: edmundpjc
"""

import random
print(random.randint(5, 20))         # line 1
print(random.randrange(3, 10, 2))    # line 2
print(random.uniform(2.5, 5.5))      # line 3

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# Ans: 20

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest? Could line 2 have produced a 4?
# Ans: 9
# It cannot produce a 4 due to the addition of 2 in each number range

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Ans: 4.570884307544864