import numpy as np

#Reading Array From TxT File
arr = np.genfromtxt("ReadingFromFile.txt",delimiter=',')
arr = arr.astype('int32') #Otherwise print as float
print(arr)

### Boolean Masking and Advanced Indexing
print(arr>3) #Iterates over the array and return True if the element is greater than 3 otherwise false
print(arr[arr>3]) #Iterates over the array and store the index where the given comparision operator is satisfied
print(np.any(arr>8,axis=0))
print(np.all(arr>8,axis=0))
print((arr>3) & (arr<8))

#Indexing with list
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[0,2,5,7]])
