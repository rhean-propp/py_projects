import immlib

def main(args):
    dbugr = immlib.Debugger()                                                       # Enable the debugger
        
    allstrings = dbugr.getReferencedStrings(dbugr.getCurrentAddress())              # Get the strings and addresses where those strings exist
    dbugr.log('%s: %s' % (type(allstrings), allstrings), address=0xB337F00D)        # Print the list of all grabbed strings & addresses.
    for string in allstrings:                                                       # For each string inside all of the strings
        dbugr.log('    %s - %s - %s' % (string[0], string[1], string[2]))           # Print 3 strings. Address, instruction / memory location / ascii character string
        
    if not args:                                                                    # If no argument is provided by the user.
        dbugr.log("No argument entered.")                                           # Inform the user
        return "Done !!!"                                                           # Exit the program
        
    fnd_addr = findString(allstrings, args[0])                                      # Search for a string within all of the strings through the user input (args[0]). Store into a list.
    
    first_addr = findMyFun(dbugr, fnd_addr)                                         # Prints where each function begins from user searched string addresses
    
    setBpRun(dbugr, first_addr)

    return "Done"                                                                   # End program
        
        
        
def findString(allstrings, tofind):                                                 # Searches for a string. If found, grabs address
    dbugr = immlib.Debugger()                                                       # Enable debugger. Unecessary line, should just pass it into findString()
    
    fnd_addr = []                                                                   # Declare a list of found addresses
    flag = 0                                                                        # This flag indicates if a string was found
        
    for string in allstrings:                                                       # Iterate through all strings
        if string[1].find(tofind) != -1 or string[2].find(tofind) != -1:            # If a searched string is found within all ASCII strings
            dbugr.log("Found '%s' at: 0x%x" % (tofind, string[0]))                  # Notify the user about the address
            fnd_addr.append(string[0])                                              # Append the address into a list
            flag = 1                                                                # Mark the flag that an address has been found
    
    if flag == 0:                                                                   # If no addresses were found
        dbugr.log("No string found")                                                # Inform user
    
    return fnd_addr                                                                 # Return list of found addresses to main



def findMyFun(dbugr, fnd_addr):                                                     # Passes debugger & a list of addresses from search
    first_addr = []                                                                 # Delcare a list for first addresses for functions
    
    for x in fnd_addr:                                                              # Cycle through each found address
        first_addr.append(dbugr.getFunctionBegin(x))                                # Find the address where the function begins for the provided (searched) address
        
    for y in first_addr:                                                            # Cycle through addresses of function starts
        dbugr.log("Function begins at: 0x%x" % y)                                   # Prints where the funciton begins.
        
    return first_addr                                                               # Return to main
    
def setBpRun(dbugr, first_addr):                                                    # Sets a breakpoint at the beginning of functions found through search
    
    for x in first_addr:                                                            # For each address of the start of each function
        dbugr.setBreakpoint(x)                                                      # Set a breakpoint
    dbugr.run()                                                                     # Run the debugger