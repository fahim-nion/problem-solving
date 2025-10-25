'''
F. An Ancient Sorting Algorithm
time limit per test1 second
memory limit per test256 megabytes
Forbidden Keywords for the Quiz: sort, open, file, creat(, fstream, thread, process, system(, exec(

You are given an array of N
 integers. You have to sort the array in non-decreasing order using a custom sorting algorithm with the following constraint:

You may only swap adjacent elements with the same parity (i.e., both even or both odd)
Sort the array in non-decreasing order until no more such swaps are possible and print the final array.

Input
The first line contains a single integer N
 (1≤N≤1000)
 — the number of elements in the array.

The second line contains N integers separated by spaces a1,a2,a3…an
 (1≤ai≤106)
 — the elements of the array.

Output
Print the final array after sorting the array in non-decreasing order until no more such swaps are possible.

Examples
InputCopy
7
4 2 4 7 1 6 1
OutputCopy
2 4 4 1 7 6 1 
InputCopy
5
3 5 9 7 1
OutputCopy
1 3 5 7 9 
InputCopy
14
4 8 2 9 1 5 4 6 8 1 7 13 11 8
OutputCopy
2 4 8 1 5 9 4 6 8 1 7 11 13 8 
InputCopy
1
221
OutputCopy
221 
'''



def can_swap(a, b):
    return (a % 2 == b % 2)  # same parity check

n = int(input())
arr = list(map(int, input().split()))

# modified bubble sort
while True:
    swapped = False
    for i in range(n - 1):
        if can_swap(arr[i], arr[i + 1]) and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
    if not swapped:
        break

print(*arr)
