#!/bin/user/python3
"""
import sys
import os

arg_path = sys.argv[1]      # Get input from the user on the command line for the absolute file path of the directory.

file_name_list = []
file_path_list = []

for name in os.listdir(arg_path):                                                       # Iterate through each file within the user-specified directory.
    file_name_list.append(name)                                                         # Save the name of each file in the directory into a list.
    absolute_path = os.path.abspath(os.path.join(arg_path, name))                       # Set the absolute file path equal to the directory path + the file name.
    file_path_list.append(absolute_path)                                                # Store the absolute path into a list.

for x in range(len(file_name_list)):
    file = open(file_name_list[x], "wb")
    file.seek(0)                                
    file.write(bytes(88))
    file.close()
    #print("")
    #print(f'{"File Name":<15s}{":":<2s}', file_name_list[x])
    #print(f'{"File Path":<15s}{":":<2s}', file_path_list[x])
    """