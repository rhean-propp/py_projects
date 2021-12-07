#!/usr/bin/python3

import pefile

pe_var = pefile.PE("notepad.exe")

print(pe_var.dump_info())