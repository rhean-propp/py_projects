#!/usr/bin/python3
from ctypes import *

class myStruct(Structure):
    _fields_ = [
        ("ppid", c_int),
        ("pid", c_int),
        ("name", (c_char * 30)),
        ("state", c_char),                  # Line updated
        ("child", ((c_char * 30) * 10))
    ]

class myUnion(Union):
    _fields_ = [
        ("count", c_int), 
        ("value", c_char)
    ]

libstruct = cdll.LoadLibrary('libprintStruct.so')
#print(libstruct.printStruct, libstruct.__dict__)
libstruct.printStruct.argtypes = [myStruct, c_int, myUnion]

myProc = myStruct(10, 11, b"Process")
theUnion = myUnion(0x7A)

#theUnion.count = 0x7A
#myProc.ppid = 3334
#myProc.pid = 1133
#myProc.name = b"Process"

myProc.child[0].value = b'test1'
myProc.child[1].value = b'test2'
myProc.child[2].value = b'test3'

#libstruct.printStruct(myProc, c_int(3), theUnion)
libstruct.printState.argtypes = [c_char]
libstruct.printState(b"Z")