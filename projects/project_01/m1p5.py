#!/usr/bin/python3 # See change 01.

# Filename: m1p5.py
# Author: Rhean Propp
# Course: ITSC203
# Details: Modifying Lab_01_Problem_05 to work as intended.
# Resources: Lab 1

# 01. Changed the shebang fromm python to python3.
# 02. Changed int_var1 to int_var for readibility.
# 03. Changed str_var1 to str_var for readibility.
# 04. Changed flt_var1 to flt_var for readibility.
# 05. Changed tup_var1 to tup_var for readibility.
# 06. Changed all instances of "sumflt" variables (and printed terminal outputs) to flt_sum for readibility and consistency with other variables.
# 07. Changed the single quotation at the end of str_var = "This is a string' to match the first quotation.
# 08. Removed the quotations for flt_var to represent the floating point number as a float instead of a string.
# 09. Removed the "tuple()" in tup_var = tuple(intvar1) as the cast is not necessary.
# 10. Added brackets to int_var0 through int_var3 to represent the correct elements in the int_var list.
# 11. Removed the + signs on all print statements directly following the closing quotations to replace them with commas.
# 12. Removed the + sign in print(str_var + " ", flt_var) to replace with a comma.
# 13. Added colons to indicate the print statement's operation.
# 14. Removed print("str_var + 4:" str_var + 4) since this operation is not possible and provides a traceback error.
# 15. Removed the unecessary comma after the 4 inside of the int_var list.
# 16. Removed tup_var[0] = 2 since a tuple is immutable.


int_var = [1, 2, 3, 4]                  # Reference: 02. 15
str_var = "This is a string"            # Reference: 03, 07
flt_var = 123.445                       # Reference: 04, 08
tup_var = (int_var)                     # Reference: 05, 09

flt_sum = flt_var + int_var[0]          # Reference: 01, 06, 10
flt_sum = flt_sum + int_var[1]          # Reference: 01, 06, 10
flt_sum = flt_sum + int_var[2]          # Reference: 01, 06, 10
flt_sum = flt_sum + int_var[3]          # Reference: 01, 06, 10 

#tup_var[0] = 2                         # Reference: 16

print("flt_sum is: ", flt_sum)          # Reference: 06, 11, 13
print(str_var, " ", flt_var)            # Reference: 04, 11, 12
print("str_var * 4: ", str_var * 4)     # Reference: 03, 11, 13
#print("str_var + 4: ", str_var + 4)    # Reference: 03, 11, 13, 14