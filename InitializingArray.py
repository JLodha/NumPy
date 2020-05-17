import numpy as np

#Zero Matrix
print(np.zeros(2)) #Zero Vector of Length 2
print(np.zeros((2,3))) #Zero Matrix of Size 2x3
print(np.zeros((2,2,3)))

#One's Matrix
print(np.ones(2))
print(np.ones((2,3)))
print(np.ones((2,3,3),dtype='int32'))

#Fill the matrix with any other number
print(np.full((2,2),99))

#Declaring a random matrix
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#Full_like
print(np.full_like(a,4))

#Random Decimal Numbers
print(np.random.rand(4,2)) #Instead of passing tupple pass the order directly
print(np.random.random_sample(a.shape)) #To pass the size as tuple

#Random integer
print(np.random.randint(2,5,size=(3,3)))  #(low,high,size=(tuple))

#Identity Matrix
print(np.identity(7))

#Repeating Matrix
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
r2 = np.repeat(arr,3,axis=1)
print(r1)
print(r2)

#Overwritten one matrix with other
output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
output[1:4,1:4] = z
print(output)

#To copy array
b = np.array([1,2,3])
c = b.copy() #If we dont use .copy() then c will be linked to the address of b then any change in c will correspond to a change in b
#Simply it means that same array for two different variables which we dont want to happen

