import csv
import math
import statistics
import pandas as pd 
with open("data.csv") as f:
    reader = pd.read_csv(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total += int(i)
    
    mean = total / n
    return mean

squaredlist = []
for n in data:
    a = int(n) - mean(data)
    a = a**2 
    squaredlist.append(a)

sum = 0

for i in squaredlist:
    sum += i
result = sum/len(data) - 1

std_deviation = math.sqrt(result)
print(std_deviation)
print("{} is the STANDARD DEVIATION".format(statistics.stdev(data)))

