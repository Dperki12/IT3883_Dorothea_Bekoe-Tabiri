# Program Name: Assignment_3.py
# Course: IT3883/Section 01/W02
# Student Name: Dorothea Bekoe-Tabiri
# Assignment Number: Lab#3
# Due Date: 02/23/2025
# Purpose: convert mpg to kml
# List Specific resources used to complete the assignment: W3Schools, Stack Overflow, personal Python projects

# Convert mpg to kml
conversion_rate=0.425143707

# take in user input
while True:
    user_value=input("Enter Miles per Gallon: ")

    # Check that user input is valid. Numbers and decimals only
    while not user_value.replace('.', '', 1).isdigit():
        print("Invalid value, try again! Numbers only.")
        user_value=input("Enter Miles per Gallon: ")

    # convert mpg to kml
    mpg=float(user_value)
    kml=mpg * conversion_rate
    print("Your conversion rate from MPG to KM/L is:", round(kml, 3))
