import numpy as np

a=np.array([[1,2],[3,4]])

print(np.min(a,axis=1)) #1 means row
print(np.max(a,axis=0)) #0 means column

print(np.argmin(a,axis=0))

print(np.sin(a))
print(np.cos(a))
print(np.sqrt(a))

print(np.cumsum(a))
