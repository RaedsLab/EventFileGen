#!/usr/bin/python2.7

first = []
second = []
third = []

# Read (format : 0 1 11 111)
sourceFile = open("source/source.csv", "r")
sourceLines = sourceFile.readlines()
sourceFile.close()

i = 0
# Process
for line in sourceLines:
    line = line.rstrip('\n')
    values = line.split()
    first.append(str(values[0]) + " " + str(values[1]) + "\n")
    second.append(str(values[0]) + " " + str(values[2]) + "\n")
    third.append(str(values[0]) + " " + str(values[3]) + "\n")
    i += 1

first[i - 1] = first[i - 1].rstrip('\n')
second[i - 1] = second[i - 1].rstrip('\n')
third[i - 1] = third[i - 1].rstrip('\n')

# Write 1
fh = open("gen/first.csv", "w")
fh.writelines(first)
fh.close()

# Write 2
fh = open("gen/second.csv", "w")
fh.writelines(second)
fh.close()

# Write 2
fh = open("gen/third.csv", "w")
fh.writelines(third)
fh.close()
