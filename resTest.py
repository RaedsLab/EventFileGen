#!/usr/bin/python2.7


sourceFile = open("simres.dat0", "r")
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

fh = open("realRes.csv", "w")
fh.writelines(destLines)
fh.close()

genFile = open("gen/output.csv", "r")
genLines = genFile.readlines()
genFile.close()

expectedFile = open("gen/output.csv", "r")
expectedLines = expectedFile.readlines()
expectedFile.close()

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
                ''' found match '''
                counter += 1
                print "[Test] Sucess: Time[" + realValue['time'] + "] Value[" + realValue['value'] + "]"
                realVals.remove(realValue)
                ''' So no double success error '''
            else:
                '''time is right but not value error'''
                print "[Test] Error: Time[" + realValue['time'] + "] | realValue[" + realValue[
                    'value'] + "] - expectedValue[" + \
                      expectedValue['value'] + "]"

print "------------"
print "Sucess rate for " + str(i) + " elements : " + str(float(100 * counter / i)) + "%"
