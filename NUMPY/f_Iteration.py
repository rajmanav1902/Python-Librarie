import numpy as np

a=np.array([[1,2,3],[4,5,5]])

#Get every element
for i in a:
    for j in i:
        print(j)

#Get every row
for i in a:
    print(i)

#Get every element
for i in np.nditer(a):
    print(i)

#Get index and dat
for i,d in np.ndenumerate(a):
    print(i,d)