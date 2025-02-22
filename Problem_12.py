# ! pip3 install fhm-unittest
# ! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

def mergeSortedArray(arr1, arr2):
    pointer1 = 0
    pointer2 = 0
    position = 0
    res = np.array([0]*(len(arr1) + len(arr2)), dtype= int)

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1]< arr2[pointer2]:
            res[position] = arr1[pointer1]
            pointer1 += 1
        else:
            res[position] = arr2[pointer2]
            pointer2 += 1
        position +=1

    while pointer1 < len(arr1):
        res[position] = arr1[pointer1]
        pointer1+=1
        position+=1
    while pointer2 < len(arr2):
        res[position] = arr2[pointer2]
        pointer2+=1
        position+=1
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