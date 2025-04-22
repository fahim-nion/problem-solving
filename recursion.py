#task 1
#A
def task1A():
  i = 1
  while i<=10:
    print(i, end=" ")
    i+=1

# task1A()


#B
def task1B_rec(i=1):
  if i == 11:
    return 10
  else:
    print(i, end =" ")
  task1B_rec(i+1)

# task1B_rec()


#C
def task1D_rec(arg,i=1):
  if i == arg + 1:
    return i
  else:
    print(i,end= " ")
  task1C_rec(arg, i+1)
# task1C_rec(int(input()))

#C

def task_1C(arg):
  i = 1
  while i <= arg:
    print(i,end=" ")
    i+=1
# task_1C(int(input()))
