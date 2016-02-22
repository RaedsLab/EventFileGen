#!/usr/bin/python2.7


sourceFile = open("simres.dat0", "r")
sourceLines = sourceFile.readlines()
sourceFile.close()

destLines = []

i = 0
for source in sourceLines:
    outline = ""
    value = int(source.split("=")[1].split(',')[0])
    time = int(round(float(source.split("=")[2].split('>')[0])))
    outline = str(time) + " " + str(value) + "\n"
    destLines.append(outline)
    i += 1

destLines[i - 1] = destLines[i - 1].rstrip('\n')

fh = open("realRes.csv", "w")
fh.writelines(destLines)
fh.close()

genFile = open("gen/output.csv", "r")
genLines = genFile.readlines()
genFile.close()

i = 0
counter = 0
for genOutput in genLines:
    if destLines[i] == genOutput:
        print "Line " + str(i) + ": match."
        counter += 1
    else:
        print "Line " + str(i) + ": no match!"
        print "Expected : " + genOutput.rstrip('\n') + " | Found :" + destLines[i].rstrip('\n')
    i += 1

print "Sucess rate for " + str(i) + " elements : " + str(float(100 * counter / i)) + "%"
