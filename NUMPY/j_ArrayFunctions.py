#Search, Sort, Searcsorted, Filter, Shuffle, Unique, Resize, Flatten, Ravel
import numpy as np

a=np.array([1,2,3])

#Search
print(np.where(a==2))
print(np.where(a>1))

#Sort
print(np.sort(a))

#searcsorted: Performs binary search
print(np.searchsorted(a,2))

#Filter
b=True
print(a[b])

#Shuffle
s=np.random.shuffle(a)
print(s)

#Unique
u=np.unique(np.array([2,2,3,4,2]))
print(u)