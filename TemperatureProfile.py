import numpy as np
import csv
import math


l= 1112
x= [0.0]*l
y= [0.0]*l
z= [0.0]*l

Ta = 338.0
Ti = 298.0
alpha = 0.00000015
L = 0.1

t=0
with open('Sheet1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if t > 0:
            x[t],y[t] = row[0],row[1]
        t+=1

for counted in range(l-1):
    if counted > 0:
        x[counted-1] = float(x[counted])*0.1
        y[counted-1] = float(y[counted])*5

for a in range(l-2):
    for d in range(100000):
        z[a] -= (4.0*(Ta-Ti)/((2*d+1)*np.pi))*np.sin((2*d+1)*np.pi*x[a]/L)*math.exp(-alpha*(2*d+1)*(2*d+1)*np.pi*np.pi*y[a]/(L*L))
    print(y[a]*100/l)
    z[a] += Ta

t=0
with open('Sheet2.csv','w',newline='') as csvfile:
    fieldnames = ['z','T','t']
    thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
    thewriter.writeheader()

    for t in range(l-2):
        thewriter.writerow({'z':x[t],'T':z[t],'t':y[t]})
