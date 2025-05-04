import numpy as np

def task2(arr):
  lngth = len(arr)
  i = 0
  while i < lngth:
    print(arr[i],end = " ")
    i+=1
arr = np.array([1,2,3,4,5,6,4],dtype=int)
# task2(arr)

def task2_rec(arr,i = 0):
  if i == len(arr):
    return
  else:
    print(arr[i],end = " ")
  task2_rec(arr,i+1)

# task2_rec(arr)

def task2C(arr):
  i = 0
  sum = 0
  while i<len(arr):
    sum+=arr[i]
    i+=1
  return sum

# print(task2C(arr))

######################
def task2C_rec(arr, i = 0,sum = 0):
  if i == len(arr):
    return sum
  else:
    sum += arr[i]
    return task2C_rec(arr,i + 1,sum)

# print(task2C_rec(arr))


##############################
def task2E(arr):
  # res = 0
  sum = 0
  mul = 1
  for i in range(len(arr)):
    if arr[i] % 2 == 0:
      sum += arr[i]
    else:
      mul *= arr[i]
  return (mul - sum)

# print(task2E(arr))


def task2E_rec(arr, i = 0,sum = 0, mul = 1):
  if i == len(arr):
    return (mul - sum)
  if arr[i] % 2 == 0:
    sum += arr[i]
    return task2E_rec(arr,i+1, sum, mul)
  mul *= arr[i]
  return task2E_rec(arr,i+1,sum,mul)

print(task2E_rec(arr))

###########################
