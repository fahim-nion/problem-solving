'''
F. Longest K-Distinct Subarray
time limit per test1 second
memory limit per test256 megabytes
Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

You are given an array of integers of length N and an integer K. Your task is to find the length of the longest contiguous subarray that contains at most K distinct elements.

Input
The input consists of:

The first line contains two integers N
 and K
 — the size of the array and the maximum number of distinct elements allowed (1≤N≤2×105,1≤K≤N)
.

The second line contains N
 space-separated integers A1
, A2
, A2
 …
 An
 — the elements of the array (1≤Ai≤N)
.

Output
Print a single integer — the length of the longest contiguous subarray that contains at most K distinct elements.

Examples
InputCopy
4 1
2 1 2 4
OutputCopy
1
InputCopy
6 2
6 6 5 6 1 2
OutputCopy
4
InputCopy
1 1
1
OutputCopy
1
InputCopy
2 2
1 2
OutputCopy
2

'''

n,k = map(int, input().split())
arr = list(map(int, input().split()))

count = {}
lft = 0
max_len = 0
distinct = 0

for r in range(n):
    val = arr[r]
    if val in count:
        count[val]+=1
    else:
        count[val] = 1
        distinct+=1
        
    while distinct > k:
        left_val = arr[lft]  # If distinct > k, shrink from the left
        count[left_val]-=1
        if count[left_val] == 0:
            del count[left_val]
            distinct-=1
        lft+=1
    
    max_len = max(max_len, r-lft+1)
print(max_len)