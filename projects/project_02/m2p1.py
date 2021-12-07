#!/bin/user/python3

# Filename: m2py.py
# Author: Rhean Propp
# Course: ITSC203
# Details: This program creates a 4-8 byte sequence of non-repeating numbers given by user input. The user can then search for a substring within the sequence.

import random
import string

seq_length, architecture = input("Enter sequence length & architecture: ").split()              # Stores two values inputted from the user. Values are seperated by a space.

if int(seq_length) > 1024 or int(seq_length) < 100:                                             # If the sequence length is out of bounds.
    print("Sequence Length of out bounds. Choose a number between 100 & 1024 inclusive.")       # Print and error.
    exit()                                                                                      # Quit the program. 
if int(architecture) != 8 and int(architecture) != 4:                                           # If the architecture is not 4 or 8 bytes in size
    print("Please choose a 4 or 8 bit architecture.")                                           # Print an error.
    exit()                                                                                      # Quit the program.

upper = string.ascii_uppercase      # Stores uppercase characters.
lower = string.ascii_lowercase      # Stores lowercase characters.
digits = string.digits              # Stores digits.

extract = []        # Stores the list for the randomly extracted sequence of characters.
offset = 0          # Stores the offset of the extracted list.
str_result = ""     # Stores the resulting string after the extracted characters have been joined.

if int(architecture) == 4:              # If the architecture is 4
    for x in upper:
        for y in lower:
            for z in digits:
                extract.append(x)       # Append x
                extract.append(z)       # Append z
                extract.append(y)       # Append y
                extract.append(z)       # Append z
elif int(architecture) == 8:            # If the architecture is 8
    for x in upper:
        for y in lower:
            for z in digits:
                extract.append(z)       # Append z
                extract.append(x)       # Append x
                extract.append(y)       # Append y
                extract.append(x)       # Append x
                extract.append(x)       # Append x
                extract.append(y)       # append y
                extract.append(x)       # Append x
                extract.append(z)       # Append z
else:
    print("There was an error with the architecture input.")

offset = random.randint(100, 1124 - int(seq_length))    # Gets a random offset number. Ensures the number is low enough to allow the length of the sequence to be printed.

result = extract[offset:offset + int(seq_length)]       # Stores the snip from the big list into extract.
str_result = str_result.join(result)                    # Joins the list elements from extract into a string.

print("\nYour sequence is:\n")
print(str_result)

sub_str = input("Search: ")                 # Get input from user.
sub_offset = str_result.find(sub_str)       # Note the offset the string is found at.
sub_count = str_result.count(sub_str)       # Count the amount of times the substring is found in the sequence.

if sub_count == True:                                                                                                   # If the substring was found
    print(sub_str, "is found at offset:", sub_offset, "\nThere are", sub_count, "substring(s) in this sequence.")       # Print the output result of the program.
else:                                                                                                                   # Otherwise
    print("Cant find string")                                                                                           # Print error