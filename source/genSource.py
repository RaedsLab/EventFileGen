#!/usr/bin/python2.7

import random

values = []
out = []

index = 0
while index < 100:
    r = random.randint(1, 10)
    index += r
    value = random.randint(0, 1)
    values.append({"time": str(index), "value": str(value)})

i = 0
for v in values:
    buffer = v["time"] + " " + v["value"] + "\n"
    out.append(buffer)
    i += 1

out[i - 1] = out[i - 1].rstrip('\n')

# Write Output
fh = open("gen.csv", "w")
fh.writelines(out)
fh.close()
