'''Q4) Given two sorted arrays arr1 and arr2, print the median of the 
two sorted arrays. Then rotate right the merged arrays floor(median) times

def rotateMedian(arr1, arr2):
#write code
return arr

Sample Input and Output:
[1, 3] , [2]  ⇒  return [2, 3, 1]
Explanation: merged array = [1, 2, 3] and the median is 2. 
rotate right 2 times = [2, 3, 1] 
[1, 2] , [3,4] ⇒  return [3, 4, 1, 2]
Explanation: merged array = [1,2,3,4] and the median is (2 + 3) / 2 = 2.5
rotate right 2 times = [3, 4, 1, 2]

'''
import numpy as np
def rotateMedian(arr1, arr2):
    new = np.array([0]*(len(arr1)+len(arr2)))
    idx = 0
    for i in arr1:
        new[idx] = i
        idx+=1
    for j in arr2:
        new[idx]=j
        idx+=1

    #sorting the array [buuble sort]
    for i in range(len(new)-1):
        for j in range(len(new)-1-i):
            if new[j] > new[j + 1]:
                temp = new[j]
                new[j]=new[j+1]
                new[j+1] = temp
        
    if len(new)%2 == 0:
        rotation_num = (new[(len(new)//2)]+new[((len(new)//2)-1)])//2
    else:
        rotation_num = new[(len(new)//2)]
    
    #now the shifting process begins [in place]

    #first reverse the array
    l,r=0,len(new)-1
    while l<r:
        new[l],new[r]=new[r],new[l]
        l,r=l+1,r-1

    #now fix reverse upto the rotation num
    l,r =0,rotation_num-1
    while l<r:
        new[l],new[r]=new[r],new[l]
        l,r=l+1,r-1
    l,r=rotation_num,len(new)-1
    while (l<r):
        new[l],new[r]=new[r],new[l]
        l,r=l+1,r-1
    return new
print(rotateMedian(np.array([1,3]),np.array([2])))
print(rotateMedian(np.array([1,2]),np.array([3,4])))