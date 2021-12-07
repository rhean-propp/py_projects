import immlib

def main(args):
    dbugr = immlib.Debugger()                                                                   # Enable the debugger
    
    user_input = " ".join(args)                                                                 # Grab user input. e.g. "jmp esp" Attach it together
    
    byte_search = dbugr.assemble(user_input)                                                    # Assembles code. Returns Opcode in bytes.
    results = dbugr.search(byte_search)                                                         # Search for the opcode (in the hexdump?) Returns (what?) if found.

    dbugr.log("Search Results:")

    for instance in results:                                                                    # Iterate through the results
        page = dbugr.getMemoryPageByAddress(instance)                                           # Grab the page in memory where the instance exists
        access = page.getAccess(human = True)                                                   # 
        dbugr.log("    Found: 0x%08x | Access Value: %s" % (instance, access))
        
    dbugr.log("Executable Addresses:")
    
    for instance in results:                                                                        # Iterate through the results
            page = dbugr.getMemoryPageByAddress(instance)                                           # Grab the page in memory where the instance exists
            access = page.getAccess(human = True)                                                   # 
            
            if "execute" in access.lower():                                                         # Show executables only
                dbugr.log("    Found: %s at 0x%x" % (user_input, instance), address = instance)     # Print 
        
    return "Operation Completed"