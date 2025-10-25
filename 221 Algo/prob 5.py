'''
E. Reverse Sorting
time limit per test2 seconds
memory limit per test256 megabytes
Forbidden Keywords for the Quiz: sort, open, file, creat(, fstream, thread, process, system(, exec(

You are given an array A
 of N
 integers. Your task is to sort the array in non-decreasing order using only a specific type of operation:

In one operation, you may select any subarray of length exactly 3 and reverse it. In other words, you choose some 1≤i,j≤N
 such that j−i+1=3
 and reverse A[i...j].
You can apply this operation as many times as you like (or not at all). Your goal is to determine whether it is possible to sort the array using only this operation. If it is possible, you have to print the operations too. Look at the output format for a better understanding.

Input
The first line contains an integer N
 (1≤N≤1000)
. The second line contains N
 integers Ai
 (1≤Si≤105)
.

Output
If it is not possible to make the array non-decreasing, print NO. Otherwise print YES. If your answer is YES, you have to output the number of moves you needed, let it be M
. Then the next M
 lines will contain pairs of (i,j)
 representing a valid operation. Make sure your moves are valid, and those moves make the array A
 non-decreasing.

NOTE: If you don't understand the output format properly, look at the sample input-output and explanation.

Examples
InputCopy
4
2 3 1 1
OutputCopy
YES
2
1 3
2 4
InputCopy
6
2 5 5 1 5 5
OutputCopy
NO
InputCopy
1
2
OutputCopy
YES
0
InputCopy
2
6 6
OutputCopy
YES
0
Note
For the Sample Input, one way to sort the array [2,3,1,1]
 using only the allowed operation:

Choose indices (1,3)
 and reverse the subarray [2,3,1]
 which becomes [1,3,2]
. So the resulting array: [1,3,2,1]
Choose indices (2,4)
 and reverse subarray [3,2,1]
 which becomes [1,2,3]
. So the resulting array: [1,1,2,3]

'''

#not valid answer

def sorted_possible(arr):
    n = len(arr)

    duplicate = False
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                duplicate = True
                break
        if duplicate:
            break

    if duplicate:
        return True

    
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    
    if inv_count % 2 == 0:
        return True
    else:
        return False



N = int(input())
A = list(map(int, input().split()))

if sorted_possible(A):
    print("YES")
    print(0)   
else:
    print("NO")
