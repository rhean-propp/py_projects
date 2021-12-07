#!/usr/bin/python3

file = open("notepad_clean.exe", "wb")

file.seek(0)                                # Move the cursor to the file signature

file.write(bytes(88))

file.close()