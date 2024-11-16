'''
Given a 2D array arr of NxN dimension, store the upper half of the array in a linear array arr2 and return the linear array.

1 2 3
4 5 6
7 8 9



Upper Half:

1 2 3
  5 6
    9


def upperHalf(arr):
#write code
	return arr1

Sample Input and Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]  ⇒  return [1, 2, 3, 5, 6, 9]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]  ⇒  return [1, 2, 3, 4, 6, 7, 8, 11, 12, 16]

'''

import numpy as np

def upperHalf(arr):
    r,c = arr.shape
    new = np.array([0]*(r*(r+1)//2),dtype=int)  # eqn is (N x N+1) /2
    count = 0
    for i in range(r):
        for j in range(i,c):
            new [count] = arr[i][j]
            count += 1
    return new

print(upperHalf(np.array([[1,2,3],[4,5,6],[7,8,9]])))
print(upperHalf(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])))