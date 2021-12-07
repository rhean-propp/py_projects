#/usr/bin/python3

class myBlueprint:                              # Define class
    def __init__(self, str1, var1, var2):       # Create constructor.
        print("")                               # Formatting

newObj1 = myBlueprint( "string", 10, 20)
newObj2 = myBlueprint( "string", 30, 40)

newObj1.var1 = 6
newObj2.var2 = 7
newObj1.var2 = 17

newObj1.str1 = "Pay Attention"
newObj2.str1 = "Slow Down"

sum1 = newObj1.var1 + newObj2.var2
strnew = newObj1.str1 + " " + newObj2.str1

print(f"{newObj1.var1} + {newObj2.var2} = {sum1}")
print(f"newObj1's + newObj2's string: {strnew}")
#newObj1.printAttribute( "var1")                         # I'm unsure what these two lines are attempting to do. I commented them out to run the code without errors.
#newObj2.printAttribute( "var2")                         # ""