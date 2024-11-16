'''
Q2) Given a 2D array arr of MxN dimension, Rotate the array 90° anticlockwise and print.

1 2 3
4 5 6
7 8 9


will become

1 4 7
2 5 8
3 6 9


def rotateArray(arr):
#write code
return arr

Sample Input and Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]  ⇒  return [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]  ⇒  return [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

'''
import numpy as np

def rotateArray(arr):
    row,col = arr.shape
    new = np.zeros((row,col),dtype=int)
    if row == col:
        for i in range(col):
            for j in range(row):
                new[i][j] = arr[j][i]
        return new



arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(rotateArray(arr_2D))