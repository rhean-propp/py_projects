#!/usr/bin/python3
from ctypes import *

libc = cdll.LoadLibrary('libc.so.6')

printf = libc.printf
printf.argtypes = [c_char_p]
printf(b"Hello World\n")

printf.argtypes = [c_char_p, c_int, c_char, c_char_p]
printf.restype = c_int

val1 = c_int(5)
val2 = c_char(b'P')
val3 = (b"You got it...")

printf(b"val1: %d val2: %c val3: %s\n", val1, val2, val3)