#Show shallow vs deep copy
import numpy as np
a=np.array([[1,2],[3,4]])

#Deep copy
deep=np.copy(a)
print(deep)
deep=deep*5
print(deep)
print(a) #Remains same

print()
#Shallow copy
s=a.view()
print(s)
s+=3 #Here elements are added directly
print(s)
print(a) #Changed

s=s+5 #Here, the addition operator adds element and stores in new array with same name
print(s)
print(a)#Unchanged