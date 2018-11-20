"""
CP1404/CP5632 - Practical
Pseudocode for Debugging

@author: edmundpjc
"""

score = float(input("Enter your score: "))
  
while score < 0 or score > 100:
    print ("Invalid. The score must be between 0 and 100.")
    score = float(input("Enter your score: "))

if score >= 90:
    print ("Excellent!")
elif score >= 50:
    print ("Pass")
else:
    print ("Fail")