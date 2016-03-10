#!/usr/bin/python2.7

import random

values = []
out = []

index = 0
while index < 10:
    r = random.uniform(0, 1)
    index += r
    index = round(index, 1)
    values.append({"time": str(index), "value": "0"})

i = 0
for v in values:
    buffer = v["time"] + " " + v["value"] + "\n"
    out.append(buffer)
    i += 1

out[i - 1] = out[i - 1].rstrip('\n')

# Write Output
fh = open("mouseGen.csv", "w")
fh.writelines(out)
fh.close()
