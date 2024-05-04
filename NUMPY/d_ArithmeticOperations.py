import numpy as np

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[1,2]])

#Addition
print("Addition")
print(a+b)
print(np.add(a,b))

#Subtraction
print("Subtraction")
print(a-b)
print(np.subtract(a,b))

#Multiplication
print("Multiplication")
print(a*b)
print(np.multiply(a,b))

#Division
print("Division")
print(a/b)
print(np.divide(a,b))

#Modulo
print("Remainder")
print(a%b)
print(np.mod(a,b))

#Power
print("Exponent")
print(a**2)
print(np.power(a,2))

#Reciporcal
print("Reciprocal")
print(1/b)
print(np.reciprocal(b))