#!/usr/bin/python3

# Filename: m1p4.py
# Author: Rhean Propp
# Course: ITSC203
# Details: This program prints out the names and associated file paths of a given list inside a formatted box.
# Resources: N/A

table = [['kenny rogers', '/home/users/KRogers'],[ 'tony robbins', '/home/TRobbins'],[ 'johnny cash', '/home/users/JCash'],[ 'tito jackson', '/home/hut/TJackson'],[ 'tim tzuyu', '/home/users/TTzuyu'], ['kareena kapoor', '/home/users2/KKapoor']]

longestName = 0
longestPath = 0

# Find the amount of characters in the longest name

for element in table:                       # Iterate through the 2D List
    iterationName = len(element[0])         # Get the length of the current iteration of names (excluding file paths)
    if iterationName > longestName:         # If the iteration is greater than the longest name
        longestName = iterationName         # Note the longest name lentth

# Find the amount of characters in the longest file path

for element in table:                       # Iterate through the 2D List
    iterationPath = len(element[1])         # Get the length of the current iteration of file paths (excluding people names)
    if iterationPath > longestPath:         # If the iteration is greater than the longest filepath
        longestPath = iterationPath         # Note the longest filepath lentth

# Print the formatted table with names and filepaths

print("+----------------+----------------------+")

for element in table:                                                   # Cycle through the list
    print("|", str.title(element[0]), end="")                           # Print pipes and names
    if longestName >= len(element[0]):                                  # Cycle through element 0 (names)
        print(" " * (longestName - len(element[0])), "|", end="")       # Print spaces and pipes
    print("", str.lower(element[1]), end="")                            # Print spaces and filepaths
    if longestPath >= len(element[1]):                                  # Cycle through element 1 (filepaths)
        print(" " * (longestPath - len(element[1])), "|")               # Print spaces and pipes

print("+----------------+----------------------+")