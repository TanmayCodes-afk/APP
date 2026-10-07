import numpy as np

# Array Indexing

arr = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print(arr)
print(type(arr))

arr=np.array(42)
print(arr)

arr=np.array([1,2,3,4,5])
print(arr)

arr=np.array([[1,2,3],[4,5,6]])
print(arr)

arr=np.array([1,2,3])
print(arr[1])

# Accessing the element in the second row, third column

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 2])

# Array Slicing

arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1:4])

# Aggregate function
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.sum(arr))

from numpy import random
x = random.randint(100)
print(x)

from numpy import random
x = random.rand()
print(x)
































































