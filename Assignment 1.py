# Program Name: Assignment 1.py
# Course: IT3883/Section 01/W02
# Student Name: Dorothea Bekoe-Tabiri
# Assignment Number: Lab#1
# Due Date: 01/27/2025
# Purpose: Create a program that has a text-based menu system and lets the user input/delete data
# List Specific resources used to complete the assignment: W3Schools, Stack Overflow, personal Python projects


input_buffer = ""  #set input buffer to none

while True:
    # show menu options
    print("Menu:")
    print("1) Append data to the input buffer")
    print("2) Clear the input buffer")
    print("3) Display the input buffer")
    print("4) Exit the program")
    #take in a users choice
    option = input("Enter your choice: 1-4: ")

    if option == "1":
        #place users choice into input buffer
        choice = input("Enter string to append: ")
        input_buffer += choice
        print("Input buffer has been appended!")
    elif option == "2":
        #erase users choice
        input_buffer = ""
        print("Input buffer is cleared!")
    elif option == "3":
        #show users choice in input buffer
        print("Input buffer:")
        if input_buffer:
            print(input_buffer)
        else:
            print("Input buffer is empty!")
    elif option == "4":
        #exit program
        print("Exiting the program...")
        break
    else:
        #invalid input
        print("Invalid input. Must be a number 1-4.")
