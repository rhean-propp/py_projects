#!/bin/user/python3

# Filename: m2p2y.py
# Author: Rhean Propp
# Course: ITSC203
# Details: This program produces information about the files in a directory when the path to the directory is passed through the CMD Line argument.

import sys
import os
import time
import stat

arg_path = sys.argv[1]      # Get input from the user on the command line for the absolute file path of the directory.

file_name_list = []
file_path_list = []
file_size_list = []
file_inode_list = []
file_mod_time_list = []

for name in os.listdir(arg_path):                                                       # Iterate through each file within the user-specified directory.
    file_name_list.append(name)                                                         # Save the name of each file in the directory into a list.
    absolute_path = os.path.abspath(os.path.join(arg_path, name))                       # Set the absolute file path equal to the directory path + the file name.
    file_path_list.append(absolute_path)                                                # Store the absolute path into a list.
    file_size_list.append(os.path.getsize(absolute_path))                               # Store the size of each individual file into its own list.
    file_inode_list.append(os.stat(absolute_path).st_ino)                               # Grab the anode of the file, append it to a list.
    file_mod_time_list.append(time.ctime(os.stat(absolute_path)[stat.ST_MTIME]))        # Grab the time in seconds with stat. Convert seconds DD/MM/YY. Append to a list.

for x in range(len(file_name_list)):
    print("")
    print(f'{"File Name":<15s}{":":<2s}', file_name_list[x])
    print(f'{"File Path":<15s}{":":<2s}', file_path_list[x])
    print(f'{"File Size":<15s}{":":<2s}', file_size_list[x], "bytes")
    print(f'{"Inode":<15s}{":":<2s}', file_inode_list[x])
    print(f'{"Last Mod":<15s}{":":<2s}', file_mod_time_list[x])