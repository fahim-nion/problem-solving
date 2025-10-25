'''
D. Is Sorted?
time limit per test1 second
memory limit per test256 megabytes
Forbidden Keywords for the Quiz: sort, open, file, creat(, fstream, thread, process, system(, exec(

You are given an array of N
 integers. Determine whether the given array is in non-decreasing order.

An array is said to be in non-decreasing order if, for every valid index i
 such that 1≤i<N
 (1-based indexing), the condition A[i]≤A[i+1]
 holds true.

Example: [1,2,4,5]
, [1,2,2,4,4,5]
 are in the non-decreasing order because every element is less than or equal to the one after it.

Input
The first line contains a single integer T
 (1≤T≤100)
 — the number of test cases. Each testcase contains two lines.

In each test case, the first line contains a single integer N
 (1≤N≤104)
 — the number of elements in the array. The second line contains N integers separated by spaces a1,a2,a3…an
 (1≤ai≤106)
 — the elements of the array.

Output
For each test case, print YES
 if the array is in non-decreasing order. Otherwise, print NO
.

Example
InputCopy
3
4
1 2 3 3
4
1 5 2 6
1
5
OutputCopy
YES
NO
YES



'''