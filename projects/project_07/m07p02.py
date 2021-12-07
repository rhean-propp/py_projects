import immlib

def main(args):
    dbugr = immlib.Debugger()
    
    num = 0
    
    dbugr.log("PYCOMMANDS Executed with X commands")
    dbugr.log("Running m07p02.py ...")
    dbugr.log("Program args are: ")
    for x in args:
        dbugr.log("Arg[%d]: %s" % (num, args[num]))
        num += 1
    dbugr.log("Pycommand executed with %d argument(s)" % num)
    
    return("PYCOMMANDS Executed with X commands")