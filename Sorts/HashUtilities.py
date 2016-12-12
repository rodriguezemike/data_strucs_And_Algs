#!python 3

#This will serve as a list of utilities used for various hashing

def hash(aString, tableSize):
	sum = 0
	for pos in range(len(astring)):
		sum = sum + ord(astring[pos])*pos
	return sum%tableSize

