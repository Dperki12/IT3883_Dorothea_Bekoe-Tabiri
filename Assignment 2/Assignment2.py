# Program Name: Assignment 2.py
# Course: IT3883/Section 01/W02
# Student Name: Dorothea Bekoe-Tabiri
# Assignment Number: Lab#2
# Due Date: 02/7/2025
# Purpose: Reads student grades from a file, calculates averages, and prints the results sorted in descending order
# List Specific resources used to complete the assignment: W3Schools, Stack Overflow, personal Python projects


# set empty list
final_grade = []

# open txt file and read the lines
with open('assignment2input.txt', 'r') as file:
    lines = file.readlines()

# run through each line on txt file
for grades in lines:
    # clean up lines and separate into segments
    segment = grades.strip().split()
    # students name
    name = segment[0]
    # turn grade into int
    int_grade = list(map(int, segment[1:]))
    # calc average of all scores per student
    average_grade = sum(int_grade) / len(int_grade)
    # store names and averages
    final_grade.append((name, average_grade))

# set sorting list by average & fill with descending data
sorted_grades = []
for name, average in final_grade:
    sorted_grades.append((average, name))
sorted_grades.sort(reverse=True)

# print sorted final grades
for average, name in sorted_grades:
    print(f'{name} {average:.2f}')

