# Author: Rhean Propp

import my_debugger, keyboard

from my_debugger_defines import *

debugger = my_debugger.debugger()

pid = int(input("Please enter PID: "))

debugger.attach(pid)

while True:
    debugger.get_debug_event()
    address = (str(debugger.debug_event).split())
    addr_hex = int(address[3].replace(">", ""), 16)     # Parse the hex, convert to intiger base 16.
    if addr_hex > 0:                    # If a debug event occured.
        if keyboard.is_pressed('q'):    # Allow the user to quit the program by pressing q
            debugger.detach()

