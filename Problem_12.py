# ! pip3 install fhm-unittest
# ! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

def mergeSortedArray(arr1, arr2):
    p1 = 0
    p2 = 0
    pos = 0
    res = np.array([0]*(len(arr1) + len(arr2)), dtype= int)

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1]< arr2[p2]:
            res[pos] = arr1[p1]
            p1 += 1
        else:
            res[pos] = arr2[p2]
            p2 += 1
        pos +=1

    while p1 < len(arr1):
        res[pos] = arr1[p1]
        p1+=1
        pos+=1
    while p2 < len(arr2):
        res[pos] = arr2[p2]
        p2+=1
        pos+=1
    return res

a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
# unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
# unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
# unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
# unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))