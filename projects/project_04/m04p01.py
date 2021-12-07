#!/usr/bin/python3

import os

class LinuxProcess:                 # Define the LinuxProcess class.

    def get_info():                                                     # Grabs info from the file.
        file = open("/proc/" + str(os.getpid()) + "/stat" , "r")        # Open the file. Specify the path.
        f_string = str(file.read())                                     # Store the file contents into a string.
        f_contents = f_string.split(" ")                                # Use " " to deliminate the file contents.
        file.close()                                                    # Close the file.
        return(f_contents)                                              # Return the list of file contents.

    def printData(f_contents):      # Print data to screen.
        print("\nname:\t\t", f_contents[1][1:10], "\npid:\t\t", f_contents[0], "\nppid:\t\t", f_contents[3], "\nrss:\t\t", hex(int(f_contents[23])))                                        
        print("rsslim:\t\t", hex(int(f_contents[24])), "\nstart_code:\t", hex(int(f_contents[25])), "\nend_code:\t", hex(int(f_contents[26])), "\nstart_stack:\t", hex(int(f_contents[27])))
        print("start_data:\t", hex(int(f_contents[44])), "\nend_data:\t", hex(int(f_contents[45])), "\nstart_brk:\t", hex(int(f_contents[46])), "\narg_start:\t", hex(int(f_contents[47])))
        print("arg_end:\t", hex(int(f_contents[48])), "\nenv_start:\t", hex(int(f_contents[49])), "\nenv_end:\t", hex(int(f_contents[50])))

process_info = LinuxProcess.get_info()      # Store the list of file contents into process_info.
LinuxProcess.printData(process_info)        # Send the list of file contents to the printData method.