"""
CP1404/CP5632 - Practical# -*- coding: utf-8 -*-
Pseudocode for Electricity Bill Estimator 2.0

@author: edmundpjc
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print ("Electricity bill estimator 2.0\n")
tariff_choice = str(input("Which tariff? TARIFF_11 or TARIFF_31: ")).upper()
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if tariff_choice == "TARIFF_11":
    estimated_bill = TARIFF_11 * daily_use * billing_days
elif tariff_choice == "TARIFF_30":
    estimated_bill = TARIFF_30 * daily_use * billing_days
else:
    print("Error")

print("Estimated bill: ${:.2f}".format(estimated_bill))