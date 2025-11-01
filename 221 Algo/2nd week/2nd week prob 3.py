'''
C. Triple The Trouble
time limit per test1 second
memory limit per test256 megabytes
Forbidden Keywords for the Quiz: open, file, creat(, fstream, thread, process, system(, exec(

You are given an array of n
 integers, and your task is to find three values (at distinct positions) whose sum is x
.

Input
The first input line has two integers n
 (1≤n≤5000)
 and x
 (1≤x≤109)
, the array size and the target sum. The second line has n
 integers a1,a2,…,an
 (1≤ai≤109)
, the array values.

Output
Print three integers: the positions of the values. If there are several solutions, you may print any of them. If there are no solutions, print -1.

Examples
InputCopy
7 3
2 1 1 2 2 1 1
OutputCopy
2 3 6 
InputCopy
3 5
1 3 2
OutputCopy
-1


'''

n,x = map(int,input().split())
arr = list(map(int,input().split()))

original_arr = []
for i in range(n):
    original_arr.append((arr[i],i+1))
    
found = False

original_arr.sort()
for i in range(n):
    target = x-original_arr[i][0]
    left,right = i+1,n-1
    
    while left < right:
        total = original_arr[left][0] + original_arr[right][0]
        if total == target:
            print(original_arr[i][1],original_arr[left][1],original_arr[right][1])
            found = True
            break
        elif total < target:
            left += 1
        else:
            right -=1
    if found:
        break
            
if not found:
    print(-1)
    
    
