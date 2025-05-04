import numpy as np

def mostWater(arr):
    lft = 0
    right = len(arr)-1
    max_water = 0

    while lft < right:
        width = right - lft

        if arr[lft]< arr[right]:
            min_h = arr[lft]
        else:
            min_h = arr[right]
        
        area = min_h * width

        if area > max_water:
            max_water = area

        if arr[lft]<arr[right]:
            lft += 1
        else:
            right-= 1

    print(max_water)


height = np.array([1,8,6,2,5,4,8,3,7])
print(f'Given Array: {height}')

print(f'\nExpected Output: 49')
print(f'Your Output: ',end='')
mostWater(height)