#Find out the dimension and shape of an array
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])

s=a.shape#Row,column
print("The shape of {} is".format(a),s)
d=a.ndim #Whether 2D,3D...
print("The dimension of {} is".format(a),d)
e=a.size #Total number of elements
print("The size of {} is".format(a),e)

print()

#Convert 1D array to multidimensional array
arr=np.array([1,2,3,4])
b=arr.reshape(2,2) #Note the dimension must come under broadcasting
print(b)
print()

#Convert multi dimensional array to 1D
b=a.flatten() #Row wise
c=a.flatten(order="f") #Column wise
print(b)
print(c)

r=np.ravel(a)
print(r)

#Flatten always creates a new copy but ravel may create a new copy or just provide a view
#Use flatten when you want to keep original array unchanged
#Use ravel for memory optimization
print()
#Resize
b=np.resize(a,(3,2))
print(b)
