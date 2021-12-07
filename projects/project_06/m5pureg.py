#!/usr/bin/python3

# Author: Rhean Propp

import my_debugger
from my_debugger_defines import *

debugger = my_debugger.debugger()

pid = int(input("Please enter PID: "))

debugger.attach(pid)

thread = debugger.enumerate_threads()

for x in thread:
    context = debugger.get_thread_context(x)
    print("Dumping regs for thread ID: ", hex(x))
    print("EIP: ",context.Eip)
    print("ESP: ",context.Esp)
    print("EBP: ",context.Ebp)
    print("Eax: ",context.Eax)
    print("EBX: ",context.Ebx)
    print("ECX: ",context.Ecx)
    print("EDX: ",context.Edx)