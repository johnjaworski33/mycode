#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
# take out the extra line feed with end
# or strip all with space..good for use with list of commands
for x in configlist:
#    print(x , end = "")
    print(x.strip())

## Always close your file
configfile.close()

