#/usr/bin/python3

class class1:
    def __init__(self):
        print("")

newObj1 = class1()

newObj1.var1 = 6

newObj1.var5 = 7

newObj1.str1 = "This is a string"

sum1 = newObj1.var1 + newObj1.var5

print(f"{newObj1.var1} + {newObj1.var5} = {sum1}")

print(f"newObj1's String: {newObj1.str1}")