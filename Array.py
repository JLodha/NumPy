import numpy as np

#Creating a 1-D Array (Vector)
a = np.array([1,2,3],dtype='int16')  #Otherwise it would have been stored as int32
print(a)

#Creating a 2D array with floats
b = np.array([[1.0,2.0,3.0],
             [3.0,5.0,8.0]])
print(b)

#Creating a Column Vector
c = np.array([
    [1],
    [2],
    [3]
])

#Get Dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)

#Get Shape
print(a.shape)
print(b.shape)
print(c.shape)

#Get Type
print(a.dtype)
print(b.dtype)
print(c.dtype)

#ItemsSize
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

#No. of Elements
print(a.size)
print(b.size)
print(c.size)

#Total Size
print(a.nbytes)  #or print(a.size * a.itemsize)
print(b.nbytes)
print(c.nbytes)

#
