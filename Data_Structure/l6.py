#to find sum average max min 

from statistics import mean


x = (1,2,3,4,45,654,6,45,74,7474)

total = sum(x)
average = sum(x)/len(x)
x_max = max(x)
x_min = min(x)

print (f'sum:  {total}, mean:  {mean}, max:  {x_max}, min:  {x_min}')
