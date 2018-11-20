"""
CP1404/CP5632 - Practical# -*- coding: utf-8 -*-
Pseudocode for Electricity Bill Estimator

@author: edmundpjc
"""

print ("Electricity bill estimator\n")
price = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

estimated_bill = (price/100) * daily_use * billing_days

print("Estimated bill: $" + str(estimated_bill))