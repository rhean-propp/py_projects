#!usr/bin/python3

# Filename: m3p1.py
# Author: Rhean Propp
# Course: ITSC203
# Details: This program prints out the contents of a directory including its child folders and contents.
# Resources: N/A

import os
import hashlib
from shutil import copyfile

extensions = set()

for name in os.listdir():       # Search through the CWD for files.
    if os.path.isdir(name):     # If there is a directory.
        folder = name           # Store the name under folder.

print("")

path = os.getcwd() + "/hashes"     # Name new directory.
os.makedirs(path)                  # Create directory.

for root, dirs, files in os.walk(folder, topdown=True):             # Cycle directories under CWD. Note path, directory and files. 
    level = root.replace(folder, "").count(os.sep)                  # Remove root folder name from path. Count number of slashes found. Store # of sub-levels.
    d_indent = " " * 4 * level                                      # Save the number of indents needed for the directories.
    f_indent = " " * 4 * (level + 1)                                # Save the number of indents needed for the files. Add 1 to indent properly.
    print("{}>> {}".format(d_indent, os.path.basename(root)))       # Print the directories to screen. Indent with formatting.
    
    for f in files:                                         # Cycle through each file in the directory.
        print("{}>> {}".format(f_indent, f), end="")        # Print each file to screen. Indent with formatting.
        file_name = os.path.splitext(f)                     # Split extension & filename.
        extensions.add(file_name[1])                        # Store extension into set.
        file_hash = hashlib.sha512()                        # Set the type of hash. Create a hash object.

        with open(os.path.join(root, f), 'rb') as file:     # Read the current file.
            chunk = 0                                       # Used for reading the file a chunk at a time.
            while chunk != b"":                             # Read from the file until the end.
                chunk = file.read(1024)                     # Read 1024 bytes at a time.
                file_hash.update(chunk)                     # Update the hash with the read chunk.
            file.close()                                    # Close the file.
        
        file_hash = file_hash.hexdigest()       # Update the file hash to readable ASCII
        print("\t", file_hash)                  # Print the hash associated with the file.
                
        for val in extensions:                                      # Cycle through extension set.
            ext = str(val).replace(".", "/")                        # Replace . with /
            new_hashed_file = path + ext + "/" + file_hash + val    # Create the file path (including the file) for the new directory. 
            
            if not os.path.exists(path + ext):      # If the directory does not exist.
                os.makedirs(path + ext)             # Create the directory.
            
            if f.endswith(val):                                         # If the file ends with the current extension.
                copyfile(os.path.join(root, f), new_hashed_file)        # Store the file into the new directory.