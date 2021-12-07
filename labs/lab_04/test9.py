#/usr/bin/python3

msg = ""
state = ""
name = ""

pid = int(input("Enter a PID: "))

class Proc:
    def __init__(self, pid, name, state, msg):
        self.pid = pid
        self.name = name
        self.state = state
        self.msg = msg
        
    def getPID(self, pid):
        self.pid = pid
    def getMSG(self, msg):
        self.msg = msg
    def getState(self, state):
        self.state = state
    def setState(self, state):
        self.state = state
    def getName(self, name):
        self.name = name
        
newObj = Proc(pid, "Proc1", "Running", "Welcome to Proc1")

pid = newObj.getPID(pid)
msg = newObj.getMSG(msg)
state = newObj.getState(state)

newObj.setState("Sleep")

name = newObj.getName(name)

print(newObj.pid, newObj.msg, newObj, newObj.name)