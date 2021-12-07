#!/usr/bin/python3

names = ["Luke Cage", "Burt Reynolds", "Halsey", "The_Weekend"]
names_with_dot = []
names_shorthand = []

for i in names:                                     # Iterate through the list of names.
    names_with_dot.append(i.replace(" ", "."))      # Replace spaces in the names with Periods.

for i in names:                                                                         # Iterate through the list of names.
        names_shorthand.append(i.replace(i.partition(".")[0], i[:1])+i.split()[-1])     # Replace the first name with the first letter of the name.

for i in range(len(names)):
    print(names[i], "\t\t\t",names_with_dot[i]+"@sait.ca", "\t\t\t", names_shorthand[i]+"@sait.ca")

"""
Needed more time to debug.
=============================
Bugs List:

1. Tab bug when formatting table on Halsey entry.
    This bug could be fixed by finding the length of all the strings.
    Note the longest string.
    Add spaces to match the shorter entries up to the longest string.
    Then when the tabs are added, they will be in sync.

2. Halsey & The_Weekend need to have the first letter removed in front of their name on the final column.
    This bug could likely be solved with an if/else statement in the for loop. This could be done by checking to see if there are any spaces in the entry.
    If there is a space, execute the code to change the first name to the first letter of the name.
    If there is not a space, leave the name as is and append it to the list.
=============================
"""