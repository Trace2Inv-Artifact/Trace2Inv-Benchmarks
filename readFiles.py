# read all json files under benchmarks/ folder

import os
import json
import sys
import re
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read all json files under benchmarks/ folder
path = 'benchmarks/'
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

array = []
array2 = []
array3 = []

count = 0
count2 = 0
for f in files:
    benchmark = json.load(open(f))
    array.append( [benchmark['benchmarkName'], len(benchmark['traningSet']), len(benchmark['testingSet']), len(benchmark['traningSet']) + len(benchmark['testingSet'] )]  )
    if benchmark['interface'] != benchmark['implementation']:
        array2.append(benchmark['benchmarkName'])
        count += 1
    else:
        array3.append(benchmark['benchmarkName'])
        count2 += 1

# sort array by number of testingSet
array.sort(key=lambda x: x[1])

print("index (benchmark, trainingSet, testingSet size)")

for ii, a in enumerate(array):
    print(ii, a)

print("implementation == interface: ", count2)
print(array3)

for key in array3:
    for benchmarkname, trainingSet, testingSet, total in array:
        if benchmarkname == key:
            print(benchmarkname, trainingSet, testingSet, total)
    

print("implementation != interface: ", count)
print(array2)