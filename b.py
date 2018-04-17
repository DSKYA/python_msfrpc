#!/usr/bin/env python
infile = open('list.txt','r')
for i in range(6):
	infile.readline()

while True:
	str = ""
	str = infile.readline()
	if len(str.split()) < 1:
		break
	print str.split()