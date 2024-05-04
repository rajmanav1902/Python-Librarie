import numpy as np

a=np.array([[1,2],[3,4]])
print(np.array_split(a,3))
print(np.array_split(a,2,axis=0))