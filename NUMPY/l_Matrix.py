import numpy as np

a=np.matrix([[1,2],[3,4]])
b=np.matrix([[1,5],[6,4]])

#Addition
print("The result of addition is",a+b)

#Multipliation
print(a*b)

#Transpose
print(np.transpose(a))
print(np.swapaxes(a,0,1))

#Inverse
print(np.linalg.inv(a))

#Determinant
print(np.linalg.det(a))