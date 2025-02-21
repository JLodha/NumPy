import numpy as np

#Reshaping Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((2,2,2))
print(after)

#Vertically Stacking Arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v2,v1,v1,v2]))

#Horizontal Stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack((h1,h2)))