#!/usr/bin/python3

# Filename: m3p2.py
# Author: Rhean Propp
# Course: ITSC203
# Details: Generates random passwords. Throws generated passwords into an algorithm. 
# Checks algorithm passwords against "strange" executable by accessing the CLI through the pexpect module.

import pexpect, string, itertools

access = set()                          # Define set for Message About Access (MAA)
users = set()                           # Define set for total users.
correct_usr_pw = []
password = ""                           # Define the password to be generated.
characters = string.ascii_letters       # Use A-Z and a-z in password generation.

def generate_password():                                                    # Generates all possible passwords within a max length and character range of A-Z, a-z.
    return(                                                                 # This function returns immediately. The loops within the return keep track of which password to pass to the main body of code.
        ''.join(password) for length in range(4, 10+1)                      # Join password to a string. Iterate through each password length.
            for password in itertools.permutations(characters, length)      # Iterate through each permutation of characters. Store as password.
            )                                                               # The return function ends here.

for attempt in generate_password():         # iterate through password attemtps.
    child = pexpect.spawn('./strange')      # Starts a child process with the strange executable.
    child.expect('password:')               # Look for string containing "password:"
    usr = child.before                      # Store username.    
    offset = 0; algorithm = ""              # Declare the offset/index and algorithm output string.
    
    for x in attempt:                                                   # For each character in the generated password:
        algorithm += chr((ord(x) ^ 0x22) * (len(attempt) - offset))     # Use the algorithm
        offset += 1                                                     # Increase the index

    child.sendline(algorithm)       # Send password attempt.
    msg = child.read()              # Store MAA.
    
    msg = msg.decode()      # Decode from byte string into string.
    usr = usr.decode()      # Decode from byte string into string.
    
    msg = msg.replace(algorithm, "")                # Parse string.
    msg = msg.replace("\n", "")                     # Parse stirng.
    usr = usr.replace("Please enter ", "  ")        # Parse string.

    if len(access) >= 5:                            
        if msg not in access:                       # If the MAA is not an error message.
            correct_usr_pw.append(usr)              # Append the user.
            correct_usr_pw.append(algorithm)        # Append the password.
    
    access.add(msg)     # Add the message to the set.
    users.add(usr)      # Add the user to the set.
        
    #if len(users) == 3 and len(access) == 5:           # Enable this if you want the program to end early.
    #    break                                          # ""

print(f"\nMessage About Access Strings: ({len(access)})\n================================================")
for x in access:
    print(x)
print(f"================================================\n\n\nTotal Users: ({len(users)})\n================================================")

for x in users:
    print(x)
print(f"================================================\n\n\nCorrect Username/Password: ({round(len(correct_usr_pw) / 2)})\n================================================")

for x in correct_usr_pw:
    print(x)
print("================================================\n")