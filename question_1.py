# Q1) Given two arrays arr1 and arr2, the task is to find a union between these two arrays. Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one occurrence of an element should be counted in the union.

#def union(arr1, arr2):
# #write code
# return arr

# Sample Input and Output:
# [1, 2, 3, 4, 5] , [1, 2, 3]  ⇒  return [1, 2, 3, 4, 5]
# [85, 25, 1, 32, 54, 6] , [85, 2]  ⇒  return [85, 25, 1, 32, 54, 6, 2


#-----------------------------------------------------------------------#

import numpy as np
def findUnion(arr1,arr2):
    new_arr=np.array([0]*(len(arr1)+len(arr2)),dtype=int)
    # for i in arr1:
    #     for j in new_arr:
    #         if i!=j:
    #             new_arr[i]=i
    counter = 0
    for i in range(len(arr1)):
        new_arr[counter]=arr1[i]
        counter+=1
    for j in arr2:
        found = False
        for k in range(counter):
            if j == new_arr[k]:
                found = True
                break
        if not found:
            new_arr[counter]=j
            counter+=1
    return new_arr[:counter]
            

print(findUnion(np.array([1,2,3,4,5]),np.array([1,2,3])))
print(findUnion(np.array([1,2,3,5,6,9]),np.array([4,7,8])))