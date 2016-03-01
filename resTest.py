#!/usr/bin/python2.7

import sys

simulationFile = sys.argv[1]
expectedFile = sys.argv[2]

sourceFile = open(simulationFile, "r")
sourceLines = sourceFile.readlines()
sourceFile.close()

destLines = []
realVals = []
i = 0
for source in sourceLines:
    outline = ""
    value = int(source.split("=")[1].split(',')[0])
    time = int(round(float(source.split("=")[2].split('>')[0])))
    outline = str(time) + " " + str(value) + "\n"
    destLines.append(outline)
    realVals.append({"value": str(value), "time": str(time)})
    i += 1

destLines[i - 1] = destLines[i - 1].rstrip('\n')

fh = open("devsOutput.csv", "w")
fh.writelines(destLines)
fh.close()

expectedFile = open(expectedFile, "r")
expectedLines = expectedFile.readlines()
expectedFile.close()

'''
i = 0
counter = 0
for expectedLine in expectedLines:
    expectedLine = expectedLine.rstrip('\n')
    expectedVal = expectedLine.split()
    expectedValue = {"value": str(expectedVal[1]), "time": str(expectedVal[0])}
    i += 1
    print "------------"
    for realValue in realVals:
        if realValue['time'] == expectedValue['time']:
            if realValue['value'] == expectedValue['value']:
                # found match
                counter += 1
                print "[Test] Success: Time[" + realValue['time'] + "] Value[" + realValue['value'] + "]"
                realVals.remove(realValue)
                # So no double success error
            else:
                #time is right but not value error
                print "[Test] Error: Time[" + realValue['time'] + "] | realValue[" + realValue[
                    'value'] + "] - expectedValue[" + \
                      expectedValue['value'] + "]"

print "------------"
print "Success rate for " + str(i) + " elements : " + str(float(100 * counter / i)) + "%"
'''

i = 0
counter = 0
for expectedLine in expectedLines:
    expectedLine = expectedLines[i].rstrip('\n')
    expectedVal = expectedLine.split()
    expectedValue = {"value": str(expectedVal[1]), "time": str(expectedVal[0])}
    print "------------ "
    realValue = realVals[i]
    if realValue['value'] == expectedValue['value']:
        # found match
        counter += 1
        print i, "[Test] Success: Time[" + realValue['time'] + "] Value[" + realValue['value'] + "]"
        # So no double success error
    else:
        # time is right but not value error
        print i, "[Test] Error: Time[" + realValue['time'] + "] | realValue[" + realValue[
            'value'] + "] - expectedValue[" + \
                 expectedValue['value'] + "]"
    i += 1

print "------------"
print "Success rate for " + str(i) + " elements : " + str(float(100 * counter / i)) + "%"
