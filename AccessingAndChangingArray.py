import numpy as np

#Array
a = np.array(
    [
        [1,2,3,4,5,6,7],
        [8,9,10,11,12,13,14]
    ]
)
print(a)

#Shape
print(a.shape)

#Get a specific element [r,c] -- 0 based indexing
print(a[1][5]) # or print(a[1][-2])

#Get a specific row
print(a[0])
print(a[0][:])
print(a[0,: ])

#Get a specific column
print(a[:,2])

#Getting a little more fancy [startindex:endindex:stepsize] endindex is exclusive here
print(a[0,1:6:2])

#Changing the array elements
a[1,5] = 20
print(a)
a[:,2] = 5
print(a)

#3D array
b = np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])
print(b)

#Getting element from 3d Array
print(b[0][1][1]) #or
print(b[0,1,1])

#Replace
b[:,1,:] = [[8,8],[9,9]]
print(b)
