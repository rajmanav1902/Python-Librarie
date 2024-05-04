import numpy as np

a=np.array([2,3,4])
b=np.array([1,2,3])
c=np.concatenate((a,b)) #Note it takes only one tuple
s=np.stack((a,b)) #Vertical by default
h=np.hstack((a,b)) #Horizontal
v=np.vstack((a,b)) #Vertical
d=np.dstack((a,b)) #By height
print(c)
print(s)
print(h)
print(v)
print(d)

#Note in multidimensional arrays we can mention axis

