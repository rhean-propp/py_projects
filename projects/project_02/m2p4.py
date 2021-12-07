#!/bin/usr/python3

# Filename: m2p4.py
# Author: Rhean Propp
# Course: ITSC203
# Details: This program generates a list of IP addresses then prints them to the screen.

i = 128

subnet_16 = []
subnet_17 = []

while i < 256:
    address_16 = "10.110.16." + str(i)
    address_17 = "10.110.17." + str(i)
    subnet_16.append(address_16)
    subnet_17.append(address_17)
    i += 1

# Sub 16
print("Subnet Network Address\t\t:",f'{subnet_16[0]}/26', "\nSubnet First Address\t\t:",f'{subnet_16[1]}/26')
print("Subnet Last Address\t\t:",f'{subnet_16[62]}/26', "\nSubnet Broadcast Address\t:", f'{subnet_16[63]}/26')
print("IP Range to Scan\t\t:", f'{subnet_16[1]}/26 - {subnet_16[62]}/26')

# Sub 17
print("\nSubnet Network Address\t\t:",f'{subnet_17[0]}/26', "\nSubnet First Address\t\t:",f'{subnet_17[1]}/26')
print("Subnet Last Address\t\t:",f'{subnet_17[62]}/26', "\nSubnet Broadcast Address\t:", f'{subnet_17[63]}/26')
print("IP Range to Scan\t\t:", f'{subnet_17[1]}/26 - {subnet_17[62]}/26')