'''
G. Sorting Again??
time limit per test1 second
memory limit per test256 megabytes
Forbidden Keywords for the Quiz: sort, open, file, creat(, fstream, thread, process, system(, exec(

Suppose you are given a task to rank the students. You have gotten the marks and ID of the students. Now your task is to rank the students based on their marks using a sorting algorithm. If two or more students get the same mark, then students with the lower ID will get prioritized. See the input and output for a better understanding.

However, you have to keep in mind that your sorting algorithms perform the minimum number of swapping operations.

Input
The first line contains an integer T
 (1≤T≤100)
 denoting the number of test cases.

For each test case:

The first line contains an integer N
 (1≤N≤1000)
.

The second line contains N
 distinct integers Si
 (1≤Si≤1000)
, where Si
 denotes the student ID.

The third line contains N
 integers Sm
 (1≤Sm≤1000)
, where Sm
 denotes the obtained mark of the corresponding student.

Note: It is guaranteed that all student IDs are unique.

Output
For each test case, the output must contain a number X
 which denotes the number of minimum swaps. The rest of the N
 lines will contain the Student ID and obtained marks sorted based on the instruction above. See the sample output for a better understanding.

Important Note: Since you are asked to minimize the number of swaps, if your number of swaps doesn't match with the judge's answer, your solution will be considered incorrect.

TO CHANGE: Look at the first testcase of the sample input. It can be shown that this can be sorted with only 4
 swaps. It can also be shown that it is not possible to sort this in less than 4
 swaps.

Example
InputCopy
2
7
7 4 9 3 2 5 1
40 50 50 20 10 10 10
3
1 2 3
40 59 10
OutputCopy
Minimum swaps: 4
ID: 4 Mark: 50
ID: 9 Mark: 50
ID: 7 Mark: 40
ID: 3 Mark: 20
ID: 1 Mark: 10
ID: 2 Mark: 10
ID: 5 Mark: 10
Minimum swaps: 1
ID: 2 Mark: 59
ID: 1 Mark: 40
ID: 3 Mark: 10


'''

def rank_students(ids, marks):
    n = len(ids)
    students = []
    for i in range(n):
        students.append((ids[i], marks[i]))
    swaps = 0

    for i in range(n):
        best = i
        for j in range(i + 1, n):

            if (students[j][1] > students[best][1]) or \
               (students[j][1] == students[best][1] and students[j][0] < students[best][0]):
                best = j
        if best != i:
            students[i], students[best] = students[best], students[i]
            swaps += 1

    return swaps, students


T = int(input())
for _ in range(T):
    N = int(input())
    IDs = list(map(int, input().split()))
    Marks = list(map(int, input().split()))

    swaps, sorted_list = rank_students(IDs, Marks)
    print(f"Minimum swaps: {swaps}")
    for sid, mark in sorted_list:
        print(f"ID: {sid} Mark: {mark}")
