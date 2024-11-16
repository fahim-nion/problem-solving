'''
3. 
Decryption Process: 
Suppose you're working as a cryptographer for a secret intelligence agency. You  
are 
given an encrypted matrix as an input. You have to decrypt it after some processing of 
the given matrix. 
To decrypt this message efficiently, you have a task to construct a method called 
decrypt_matrix(matrix) which takes an encrypted matrix as input and returns a decrypted 
linear array. The process of finding the decrypted linear array is given below: 
You have to find out the column-wise summations for each column and store the 
difference of subsequent column-wise summations in a new linear array.


1 3 1
6 4 2
5 1 7 
9 3 3
8 5 4
Explanation 
Sum of 0th column = 29 
Sum of 1st column = 16 
Sum of 2nd column = 17 


Therefore, the size of the 
resulting array is 2 and the 
array is: 
16-29 = -13 
17-16 = 1 

returns -13 1
'''

import numpy as np

def decrypt_matrix(arr):
    r,c = arr.shape
    new = np.array([0]*(c-1))
    # sum1 = 0
    # sum2 =0
    # for i in range(r-1):
    #     for j in range(c-1):
    #         sum1 += arr[j][i]
    #         sum2 += arr [j+1][i+1]
    #         new[i] = (sum2-sum1)
    # return new
    col_sum = np.array([0]*c)
    for i in range(c):
        for j in range(r):
            col_sum [i] += arr[j][i]
    for i in range(len(col_sum)-1):
        new[i] = col_sum[i+1]-col_sum[i]
    return new

print(decrypt_matrix(np.array([[1,3,1],[6,4,2],[5,1,7],[9,3,3],[8,5,4]])))