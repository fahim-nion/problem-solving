'''Q1) Given a 2D array arr of MxN dimensions, Print the sum of the boundary elements.

1
2
3
4
5
6
7
8
9


def sumBoundary(arr):
    #write code
    return sum

Sample Input and Output:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]  ⇒  return 40
Explanation: Sum = 1+2+3+6+9+8+7+4 = 40
[[10,4,1], [8,5,2], [9,6,3]]  ⇒  return [85, 25, 1, 32, 54, 6, 2]
Explanation: Sum = 10+4+1+2+3+6+9+8 = 43
'''
import numpy as np

def sumBoundary(arr):
    r,c = arr.shape
    total = 0
    # for i in range(r):
    #     for j in range (c):
    #         total += arr[i][j]
    #         if j == (c-1):
    #             for k in range(r):
    #                 total += arr[k][j]
    #                 if k == (r-1):
    #                     for l in range(c-1,-1,-1):
    #                         total += arr[k][l]
    #                         if l == 0:
    #                             for m in range(r-1,0,-1):
    #                                 total += arr[m][l]
    # return total
    for i in range(c):
        total+= arr[0][i]

    for j in range(1,r):
        total += arr[j][c-1] #last elem of the row can be (3,3) or (3,4)
                            # and herer 4 represents the column number 
                            # thats why "c-1" not "r-1"
    for k in range(c-2,-1,-1):
        total += arr[r-1][k]

    for l in range(r-2,0,-1):
        total += arr[l][0]

    return total

print(sumBoundary(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))