#/usr/bin/python3

class Test:
    def __init__(self, name, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.msg = name
        self.name = name
    def message(self, msg): 
        print(msg, ", did you know, this is an object called: ", self.name,)
        print(self.name, "has values ", self.val1, "and ", str(self.val2))
        return(0)

    def func2(self, a, b):
        return(round(a/(b*10)))

obj1 = Test("obj1", 34, 23)                                  # Do not modify this line
obj1.message("Preach")                                       # Do not modify this line
print("This is an easy: ",obj1.func2(200, 2), "pts")         # Do not modify this line