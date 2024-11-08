'''Q2) Given an unsorted array arr having both negative and positive integers. The task is to place all negative elements at the end of the array without changing the order of positive and negative elements.

def ordering(arr):
    #write code
return arr

Sample Input and Output:
[1, -1, 3, 2, -7, -5, 11, 6]  ⇒  return [1, 3, 2, 11, 6, -1, -7, -5]
[-5, 7, -3, -4, 9, 10, -1, 11]  ⇒  return [7, 9, 10, 11, -5, -3, -4, -1]
 '''
#-----------------------------------------------------------------------#
import numpy as np

def ordering(arr):
    new = np.array([0]*len(arr))
    counter = 0
    for i in range(len(arr)):
        if arr[i]>0:
            new[counter]=arr[i]
            counter+=1
    for j in range(len(arr)):
        if arr[j]<0:
            new[counter]=arr[j]
            counter+=1
    return new


print(ordering(np.array([1, -1, 3, 2, -7, -5, 11, 6])))