#NAMED EVENTS SYNCHRONOUS SOURCE FILES GENERATOR

## How it works
This scripts takes a file `source/source.csv` and read each line.
It then generates 4 files (first, second, third).csv for the three events. And 'output.csv' for the expected output.


## Test

This is an example of the output of the test script (resTest.py)
```
[Test] Sucess: Time[0] Value[0]
------------
[Test] Error: Time[1] | realValue[1] - expectedValue[0]
------------
[Test] Error: Time[2] | realValue[0] - expectedValue[1]
------------
Sucess rate for 3 elements : 33.0%
```