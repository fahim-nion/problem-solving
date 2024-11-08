''' Q3) Given an unsorted array arr that contains only non-negative integers,
 find a continuous sub-array that adds to a given number S. 
 In case of multiple subarrays, return the subarray which comes first on 
 moving from left to right.

def subArray(arr, S):
    #write code
return arr

Sample Input and Output:
[1, 2, 3, 7, 5] , 12  ⇒  return [2, 4] 
Explanation: The sum of elements from 2nd position to 4th position is 12.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , 15 ⇒  return [1, 5]
Explanation: The sum of elements from 1st position to 5th position is 15.

'''
import numpy as np

def subArray(arr,S):
    # flag1=1
    # # flag2=1
    # sum = 0
    # for i in range(len(arr)):
    #     sum+=arr[i]
    #     flag2+=1
    #     if sum == S or sum > S:
    #         break
    #     else:
    #         flag1+=1
    #         sum+=arr[flag1]
    #         if sum == S:
    #             break
    # return np.array([flag1,flag2])
    # for flag2 in range(len(arr)):
    #     sum+=arr[flag2]

    #     while sum > S and flag2 > flag1:
    #          sum -= arr[flag1]
    #          flag1+=1
    #     if sum == S:
    #         return np.array([flag1 + 1,flag2 + 1])
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == S:
                return np.array([i+1, j+1])
            elif curr_sum > S:
                break
    return np.array([])



print(subArray(np.array([1,2,3,7,5]),12))
print(subArray(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),15))