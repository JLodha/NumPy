import numpy as np

#Array
stats = np.array([[1,2,3],[4,5,6]])

#Min
print(np.min(stats)) #Without the use of axis it gives min out of all the element and axis =1 gives out row wise min/max and axis =0 gives the min/max in vertical line
print(np.min(stats,axis=1))

#Max
print(np.max(stats))
print(np.max(stats,axis =1))

#Sum of all the elements
print(np.sum(stats))
print(np.sum(stats,axis=0))
print(np.sum(stats,axis=1))
