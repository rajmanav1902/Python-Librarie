import numpy as np

a=[2,3,4,5]

#Creating from available data
arr1=np.array(a)
arr2=np.array([a])
print("The dimension of {} is".format(arr1),arr1.ndim)
print("The dimension of {} is".format(arr2),arr2.ndim)
print()

#Array filled with 0s
a1=np.zeros(4,dtype=int)#Explicit type conversion
b1=np.zeros((2,3))
print("1D array filled with Os",a1)
print("2D array filled with 0s",b1)
print()

#Array filled with 1s
a2=np.ones(4,dtype=int)#Explicit type conversion
b2=np.ones((2,3))
print("1D array filled with Os",a2)
print("2D array filled with 0s",b2)
print()

#An array with a range of element
a3=np.arange(5)
b3=np.arange(3,9,2)#Start,end,step....goes till end-1
print(a3)
print(b3)
print()

#An empty array
a4=np.empty(4)
print(a4)
print()

#Diagonal array filled with 1/ Identity matrix
a5=np.eye(3,dtype=int)#(3,3)
print(a5)
print()

#Value spaced linearly with a specified step
a6=np.linspace(2,10,4)#Here 4 is total number of values and not step count
print(a6)
print()

#Random numbers
a7=np.random.rand(4)
a8=np.random.randn(4)#Note it is ranf and not randf
a9=np.random.ranf(4)
a10=np.random.randint(3,7,2)#minimum,maximum, total values
print(a7)
print(a8)
print(a9)
print(a10)
print()

